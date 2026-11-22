"""LLM generation client for OpenAI-compatible chat endpoints.

Keys are read from the environment or from ``<repo>/.env`` (never logged, never written
to outputs). Every call is recorded with prompt/evidence hashes, request settings,
latency, token usage and the raw response, so runs are auditable and resumable.
"""
from __future__ import annotations

import hashlib
import http.client
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .paths import ROOT

DEFAULT_CONFIG = ROOT / "configs" / "llm_generation.json"
TRANSIENT = {408, 409, 429, 500, 502, 503, 504, 520, 522, 524}


class FatalAPIError(RuntimeError):
    """Authentication, permission or quota problems: stop the whole run."""


def load_dotenv(path: Path = ROOT / ".env") -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_config(path: Path | str = DEFAULT_CONFIG) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def api_key_for(model: str, config: dict[str, Any]) -> str:
    for prefix, env in config["api_key_env_by_model_prefix"].items():
        if model.lower().startswith(prefix):
            key = os.environ.get(env)
            if key:
                return key
            raise FatalAPIError(f"{env} is not set (put it in .env)")
    key = os.environ.get(config["fallback_api_key_env"])
    if not key:
        raise FatalAPIError(f"No API key for model {model}")
    return key


def endpoint(config: dict[str, Any]) -> str:
    return os.environ.get(config["endpoint_env"]) or config["default_endpoint"]


def split_prompt(path: Path) -> tuple[str, str]:
    """Return (system message, user template) from a prompt Markdown file."""
    text = path.read_text(encoding="utf-8")
    system = text.split("## System message\n", 1)[1].split("\n## ", 1)[0].strip()
    user = text.split("## User message template\n", 1)[1].split("\n## ", 1)[0].strip()
    if user.count("{{EVIDENCE_JSON}}") != 1:
        raise ValueError(f"{path}: user template needs exactly one {{{{EVIDENCE_JSON}}}}")
    return system, user


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


_USE_CURL = False


def _post_curl(url: str, key: str, body: bytes, timeout: int) -> tuple[int, str]:
    """Transport via curl (used when this Python cannot open sockets, e.g. a local network filter).

    The key and headers go through curl's stdin config, so they never appear in the process list.
    """
    import subprocess
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".json") as handle:
        handle.write(body)
        handle.flush()
        config = "\n".join([
            f'header = "Authorization: Bearer {key}"', 'header = "Content-Type: application/json"',
            'header = "Accept: application/json"', 'user-agent = "pcr-revision/2.0"',
            f'data-binary = "@{handle.name}"', f"max-time = {timeout}", 'write-out = "\\n%{http_code}"',
            "silent", "show-error"])
        proc = subprocess.run(["curl", "-K", "-", url], input=config, text=True, capture_output=True)
    if proc.returncode != 0:
        raise OSError(f"curl exit {proc.returncode}: {proc.stderr.strip()[:300]}")
    text, _, status = proc.stdout.rpartition("\n")
    return int(status), text


def post(url: str, key: str, payload: dict[str, Any], timeout: int, max_retries: int) -> dict[str, Any]:
    global _USE_CURL
    parsed = urlsplit(url)
    path = parsed.path + (f"?{parsed.query}" if parsed.query else "")
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json",
               "Accept": "application/json", "User-Agent": "pcr-revision/2.0", "Connection": "close"}
    errors = []
    for attempt in range(max_retries + 1):
        conn = None
        try:
            if _USE_CURL:
                status, text = _post_curl(url, key, body, timeout)
            else:
                conn_cls = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection
                conn = conn_cls(parsed.hostname, parsed.port, timeout=timeout)
                try:
                    conn.request("POST", path, body=body, headers=headers)
                except OSError as exc:
                    if exc.errno == 9:  # EBADF: sockets blocked for this interpreter; switch transport
                        _USE_CURL = True
                        status, text = _post_curl(url, key, body, timeout)
                    else:
                        raise
                else:
                    response = conn.getresponse()
                    status, text = response.status, response.read().decode("utf-8", errors="replace")
            if 200 <= status < 300:
                return json.loads(text)
            message = f"HTTP {status}: {text[:500]}"
            if status in (401, 403) or "quota" in text.lower() or "insufficient" in text.lower():
                raise FatalAPIError(message)
            errors.append(message)
            if status not in TRANSIENT:
                raise RuntimeError(message)
        except (OSError, TimeoutError, http.client.HTTPException, json.JSONDecodeError) as exc:
            errors.append(f"{type(exc).__name__}: {exc}")
        finally:
            if conn is not None:
                conn.close()
        if attempt < max_retries:
            time.sleep(min(2 ** (attempt + 1), 30))
    raise RuntimeError("request failed after retries: " + " | ".join(errors))


def generate(prompt_path: Path, evidence_path: Path, model: str, config: dict[str, Any]) -> dict[str, Any]:
    """One generation call; returns a record ready to be written as JSON."""
    system, template = split_prompt(prompt_path)
    evidence_bytes = evidence_path.read_bytes()
    payload = {"model": model,
               "messages": [{"role": "system", "content": system},
                            {"role": "user", "content": template.replace("{{EVIDENCE_JSON}}",
                                                                         evidence_bytes.decode("utf-8"))}],
               **config["request"]}
    started, t0 = utc_now(), time.perf_counter()
    response = post(endpoint(config), api_key_for(model, config), payload,
                    config["timeout_seconds"], config["max_retries"])
    latency = round(time.perf_counter() - t0, 2)
    choice = (response.get("choices") or [{}])[0]
    content = (choice.get("message") or {}).get("content")
    ok = isinstance(content, str) and content.strip() != ""
    return {"status": "success" if ok else "invalid_response", "model": model,
            "endpoint": endpoint(config), "prompt_path": str(prompt_path.relative_to(ROOT)),
            "prompt_sha256": sha256(prompt_path.read_bytes()),
            "sent_prompt_sha256": sha256((system + "\n\n" + template).encode("utf-8")),
            "evidence_path": str(evidence_path.relative_to(ROOT)), "evidence_sha256": sha256(evidence_bytes),
            "request_settings": {k: v for k, v in payload.items() if k != "messages"},
            "started_at_utc": started, "finished_at_utc": utc_now(), "latency_seconds": latency,
            "finish_reason": choice.get("finish_reason"), "usage": response.get("usage", {}),
            "response_model": response.get("model"), "transport": "curl" if _USE_CURL else "http.client", "text": content if ok else None,
            "raw_response": response}
