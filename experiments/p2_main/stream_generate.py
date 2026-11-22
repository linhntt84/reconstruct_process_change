"""Streaming variant of pcr.llm.generate for slow models (E6, Qwen): same messages and record format.

The gateway (Cloudflare) closes a non-streaming request after 120 s without a response (HTTP 524).
With "stream": true the response arrives in chunks, so long reasoning does not hit that limit. Only the
transport differs: prompt, evidence, model and the other request settings are those of pcr.llm.generate
(minus settings dropped for the model, recorded in request_settings). Uses curl, as pcr.llm does when
Python sockets are blocked; the key goes through curl's stdin config.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from pcr.llm import FatalAPIError, api_key_for, endpoint, sha256, split_prompt, utc_now  # noqa: E402


def _stream_once(url: str, key: str, body: bytes, timeout: int) -> tuple[int, str]:
    with tempfile.NamedTemporaryFile(suffix=".json") as handle:
        handle.write(body)
        handle.flush()
        config = "\n".join([
            f'header = "Authorization: Bearer {key}"', 'header = "Content-Type: application/json"',
            'header = "Accept: text/event-stream"', 'user-agent = "pcr-revision/2.0"',
            f'data-binary = "@{handle.name}"', f"max-time = {timeout}", 'write-out = "\\n%{http_code}"',
            "no-buffer", "silent", "show-error"])
        proc = subprocess.run(["curl", "-K", "-", url], input=config, text=True, capture_output=True)
    if proc.returncode != 0:
        raise OSError(f"curl exit {proc.returncode}: {proc.stderr.strip()[:300]}")
    text, _, status = proc.stdout.rpartition("\n")
    return int(status), text


def _parse_sse(text: str) -> dict[str, Any]:
    content, reasoning, finish, usage, model = [], [], None, {}, None
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("data:"):
            continue
        data = line[5:].strip()
        if data == "[DONE]":
            break
        chunk = json.loads(data)
        model = chunk.get("model") or model
        usage = chunk.get("usage") or usage
        for choice in chunk.get("choices") or []:
            delta = choice.get("delta") or {}
            if delta.get("content"):
                content.append(delta["content"])
            r = delta.get("reasoning_content") or delta.get("reasoning")
            if r:
                reasoning.append(r)
            finish = choice.get("finish_reason") or finish
    return {"content": "".join(content), "reasoning_chars": len("".join(reasoning)), "finish_reason": finish,
            "usage": usage, "model": model}


def generate_stream(prompt_path: Path, evidence_path: Path, model: str, config: dict[str, Any],
                    timeout: int = 1800) -> dict[str, Any]:
    system, template = split_prompt(prompt_path)
    evidence_bytes = evidence_path.read_bytes()
    payload = {"model": model,
               "messages": [{"role": "system", "content": system},
                            {"role": "user", "content": template.replace("{{EVIDENCE_JSON}}",
                                                                         evidence_bytes.decode("utf-8"))}],
               **config["request"], "stream": True, "stream_options": {"include_usage": True}}
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    url, key = endpoint(config), api_key_for(model, config)
    started, t0, errors, parsed = utc_now(), time.perf_counter(), [], None
    for attempt in range(config["max_retries"] + 1):
        try:
            status, text = _stream_once(url, key, body, timeout)
            if 200 <= status < 300:
                parsed = _parse_sse(text)
                if parsed["content"].strip():
                    break
                errors.append(f"empty content (finish {parsed['finish_reason']})")
            else:
                message = f"HTTP {status}: {text[:500]}"
                if status in (401, 403) or "quota" in text.lower():
                    raise FatalAPIError(message)
                errors.append(message)
                if status not in (408, 409, 425, 429, 500, 502, 503, 504, 520, 522, 524):
                    break
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
        if attempt < config["max_retries"]:
            time.sleep(min(2 ** (attempt + 1), 30))
    ok = parsed is not None and parsed["content"].strip() != ""
    record = {"status": "success" if ok else "failed", "model": model, "endpoint": url,
              "prompt_path": str(prompt_path.relative_to(ROOT)), "prompt_sha256": sha256(prompt_path.read_bytes()),
              "sent_prompt_sha256": sha256((system + "\n\n" + template).encode("utf-8")),
              "evidence_path": str(evidence_path.relative_to(ROOT)), "evidence_sha256": sha256(evidence_bytes),
              "request_settings": {k: v for k, v in payload.items() if k != "messages"},
              "started_at_utc": started, "finished_at_utc": utc_now(),
              "latency_seconds": round(time.perf_counter() - t0, 2), "transport": "curl-stream",
              "attempt_errors": errors}
    if ok:
        record.update({"finish_reason": parsed["finish_reason"], "usage": parsed["usage"],
                       "response_model": parsed["model"], "reasoning_chars": parsed["reasoning_chars"],
                       "text": parsed["content"]})
    else:
        record["error"] = "request failed: " + " | ".join(errors)
    return record
