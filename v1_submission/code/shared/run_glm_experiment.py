#!/usr/bin/env python3
"""Run independent GLM requests for the Ostovar evidence conditions.

Security and experimental controls:
- The API key is read only from GLM_API_KEY and is never written to disk.
- Every request contains exactly one system and one user message; no chat
  history is reused between evidence conditions.
- Prompt text and model settings are fixed by versioned local files.
- Successful outputs can be resumed without repeating paid requests.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_prompt_sections(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    system_marker = "## System message\n"
    user_marker = "## User message template\n"
    constraint_marker = "## Experimental constraint\n"
    if not all(marker in text for marker in (system_marker, user_marker, constraint_marker)):
        raise ValueError(f"Prompt sections are missing from {path}")
    system = text.split(system_marker, 1)[1].split(user_marker, 1)[0].strip()
    user = text.split(user_marker, 1)[1].split(constraint_marker, 1)[0].strip()
    if user.count("{{EVIDENCE_JSON}}") != 1:
        raise ValueError("User template must contain exactly one {{EVIDENCE_JSON}} placeholder")
    return system, user


def load_index(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def build_request(
    config: dict[str, Any], system_prompt: str, user_prompt: str, output_format: str
) -> dict[str, Any]:
    payload = {
        "model": config["model"],
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": config["temperature"],
        "top_p": config["top_p"],
        "max_tokens": config["max_tokens"],
        "thinking": config["thinking"],
        "stream": config["stream"],
    }
    if output_format == "json":
        payload["response_format"] = config["response_format"]
    return payload


def post_json(
    endpoint: str,
    api_key: str,
    payload: dict[str, Any],
    user_agent: str,
    timeout: int,
    max_retries: int,
) -> dict[str, Any]:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Language": "en-US,en",
        "User-Agent": user_agent,
    }
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        # A Request/HTTP connection may no longer be reusable after a transport
        # failure.  Construct a fresh object for every retry.
        request = urllib.request.Request(
            endpoint, data=body, method="POST", headers=headers,
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"HTTP {exc.code}: {error_body}")
            if exc.code not in {408, 409, 429, 500, 502, 503, 504}:
                raise last_error
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
        if attempt < max_retries:
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"Request failed after retries: {last_error}")


def parse_assistant_json(response: dict[str, Any]) -> tuple[str | None, Any, str | None]:
    message = response.get("choices", [{}])[0].get("message", {})
    content = message.get("content")
    if content is None:
        return None, None, "Assistant message content is null"
    if isinstance(content, (dict, list)):
        return json.dumps(content, ensure_ascii=False), content, None
    if not isinstance(content, str):
        return str(content), None, f"Unsupported assistant content type: {type(content).__name__}"
    try:
        parsed = json.loads(content)
        return content, parsed, None
    except json.JSONDecodeError as exc:
        return content, None, str(exc)


def parse_assistant_text(response: dict[str, Any]) -> tuple[str | None, str | None]:
    message = response.get("choices", [{}])[0].get("message", {})
    content = message.get("content")
    if content is None:
        return None, "Assistant message content is null"
    if not isinstance(content, str):
        content = json.dumps(content, ensure_ascii=False)
    if not content.strip():
        return content, "Assistant message content is empty"
    return content, None


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("glm_experiment_config.json"))
    parser.add_argument("--prompt", type=Path, default=Path(__file__).with_name("PROMPT_V1.md"))
    parser.add_argument("--index", type=Path, default=None, help="Override the prompt-input index CSV")
    parser.add_argument("--run-id", default=None, help="Stable run directory name; required for reliable resume")
    parser.add_argument(
        "--runs-root",
        type=Path,
        default=None,
        help="Run-output directory; relative paths are resolved from the workspace",
    )
    parser.add_argument("--endpoint", default=None, help="Override API endpoint, e.g. the Z.AI international endpoint")
    parser.add_argument("--model", default=None, help="Override the configured GLM model identifier")
    parser.add_argument("--max-tokens", type=int, default=None, help="Override configured completion-token limit")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of requests for a smoke test")
    parser.add_argument("--conditions", nargs="*", default=None, help="Optional condition IDs to run")
    parser.add_argument("--repetitions", type=int, default=None, help="Override configured repetitions")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview without API calls")
    parser.add_argument("--no-resume", action="store_true", help="Repeat requests even if successful output exists")
    parser.add_argument(
        "--output-format",
        choices=("json", "markdown"),
        default="json",
        help="Expected assistant output. Markdown mode disables JSON response enforcement and writes .md files.",
    )
    args = parser.parse_args()

    workspace = args.workspace.resolve()
    config = load_json(args.config)
    if args.endpoint:
        config["endpoint"] = args.endpoint
    if args.model:
        config["model"] = args.model
    if args.max_tokens is not None:
        if args.max_tokens <= 0:
            raise SystemExit("--max-tokens must be positive")
        config["max_tokens"] = args.max_tokens
    repetitions = args.repetitions or int(config["repetitions"])
    prompt_root = workspace / "Code" / "outputs" / "ostovar_pilot" / "prompt_inputs"
    index_path = args.index or (prompt_root / "condition_index.csv")
    index_rows = load_index(index_path)
    if args.conditions:
        allowed = set(args.conditions)
        index_rows = [row for row in index_rows if row["condition_id"] in allowed]
    index_rows.sort(key=lambda row: (row["opaque_case_id"], row["condition_id"]))

    system_prompt, user_template = extract_prompt_sections(args.prompt)
    prompt_hash = sha256_text(system_prompt + "\n---\n" + user_template)
    config_hash = sha256_text(json.dumps(config, sort_keys=True))
    run_id = args.run_id or (
        "dry_run" if args.dry_run else datetime.now().strftime("%Y%m%d_%H%M%S")
    )
    runs_root = args.runs_root or Path("Code/outputs/ostovar_pilot/runs")
    if not runs_root.is_absolute():
        runs_root = workspace / runs_root
    run_dir = runs_root / run_id
    response_dir = run_dir / "responses"
    markdown_dir = run_dir / "markdown"
    partial_markdown_dir = run_dir / "markdown_partial"
    run_dir.mkdir(parents=True, exist_ok=True)
    response_dir.mkdir(parents=True, exist_ok=True)
    if args.output_format == "markdown":
        markdown_dir.mkdir(parents=True, exist_ok=True)
        partial_markdown_dir.mkdir(parents=True, exist_ok=True)

    jobs: list[tuple[dict[str, str], int]] = []
    for row in index_rows:
        for repetition in range(1, repetitions + 1):
            jobs.append((row, repetition))
    if args.limit is not None:
        jobs = jobs[: args.limit]

    manifest = {
        "run_id": run_id,
        "created_at_utc": utc_now(),
        "dry_run": args.dry_run,
        "provider": config["provider"],
        "endpoint": config["endpoint"],
        "model": config["model"],
        "settings": {
            key: config[key]
            for key in ("temperature", "top_p", "max_tokens", "thinking", "response_format", "stream")
        },
        "repetitions": repetitions,
        "prompt_path": str(args.prompt.resolve()),
        "prompt_sha256": prompt_hash,
        "config_sha256": config_hash,
        "job_count": len(jobs),
        "output_format": args.output_format,
        "independent_request_messages": ["system", "user"],
    }
    (run_dir / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    api_key = os.environ.get("GLM_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("GLM_API_KEY is not set. Export it in the shell; do not put it in source files.")
    if not args.dry_run:
        try:
            (api_key or "").encode("ascii")
        except UnicodeEncodeError:
            raise SystemExit(
                "GLM_API_KEY contains non-ASCII characters. Replace the example placeholder "
                "with the real API key; do not use the literal text KEY_CỦA_BẠN."
            ) from None

    completed = skipped = failed = 0
    for position, (row, repetition) in enumerate(jobs, start=1):
        evidence_path = workspace / row["prompt_input_path"]
        evidence_text = evidence_path.read_text(encoding="utf-8")
        evidence = json.loads(evidence_text)
        if evidence["case"]["case_id"] != row["opaque_case_id"]:
            raise AssertionError(f"Index/input mismatch: {evidence_path}")
        user_prompt = user_template.replace("{{EVIDENCE_JSON}}", evidence_text)
        request_payload = build_request(
            config, system_prompt, user_prompt, args.output_format
        )
        output_name = f"{row['opaque_case_id']}__{row['condition_id']}__r{repetition}.json"
        output_path = response_dir / output_name

        if output_path.exists() and not args.no_resume:
            previous = load_json(output_path)
            if previous.get("status") == "success":
                skipped += 1
                print(f"[{position}/{len(jobs)}] skip {output_name}")
                continue

        record: dict[str, Any] = {
            "status": "dry_run" if args.dry_run else "started",
            "run_id": run_id,
            "opaque_case_id": row["opaque_case_id"],
            "condition_id": row["condition_id"],
            "repetition": repetition,
            "prompt_input_path": row["prompt_input_path"],
            "evidence_sha256": sha256_text(evidence_text),
            "prompt_sha256": prompt_hash,
            "request_metadata": {
                "endpoint": config["endpoint"],
                "model": config["model"],
                "temperature": config["temperature"],
                "top_p": config["top_p"],
                "max_tokens": config["max_tokens"],
                "thinking": config["thinking"],
                "response_format": (
                    config["response_format"] if args.output_format == "json" else None
                ),
                "output_format": args.output_format,
                "user_agent": config["user_agent"],
                "message_count": 2,
            },
            "started_at_utc": utc_now(),
        }

        if args.dry_run:
            record["request_preview"] = {
                "system_chars": len(system_prompt),
                "user_chars": len(user_prompt),
                "evidence_items": len(evidence["atomic_evidence"]),
                "temporal_series": len(evidence.get("temporal_evidence", [])),
                "temporal_bins": sum(
                    len(series.get("bins", []))
                    for series in evidence.get("temporal_evidence", [])
                ),
                "roles": [message["role"] for message in request_payload["messages"]],
            }
            record["finished_at_utc"] = utc_now()
            output_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
            completed += 1
            print(f"[{position}/{len(jobs)}] dry-run {output_name}")
            continue

        try:
            response = post_json(
                config["endpoint"],
                api_key or "",
                request_payload,
                config["user_agent"],
                int(config["timeout_seconds"]),
                int(config["max_retries"]),
            )
            if args.output_format == "markdown":
                assistant_text, parse_error = parse_assistant_text(response)
                assistant_json = None
            else:
                assistant_text, assistant_json, parse_error = parse_assistant_json(response)
            response_message = response.get("choices", [{}])[0].get("message", {})
            finish_reason = response.get("choices", [{}])[0].get("finish_reason")
            if (
                args.output_format == "markdown"
                and parse_error is None
                and finish_reason != "stop"
            ):
                parse_error = f"Incomplete Markdown response: finish_reason={finish_reason}"
            record.update(
                {
                    "status": "success" if parse_error is None else "invalid_response",
                    "finished_at_utc": utc_now(),
                    "response_id": response.get("id"),
                    "request_id": response.get("request_id"),
                    "response_model": response.get("model"),
                    "finish_reason": finish_reason,
                    "usage": response.get("usage"),
                    "assistant_text": assistant_text,
                    "assistant_json": assistant_json,
                    "assistant_json_parse_error": parse_error,
                    "reasoning_content": response_message.get("reasoning_content"),
                    "raw_response": response,
                }
            )
            if parse_error is None:
                if args.output_format == "markdown" and assistant_text is not None:
                    markdown_name = output_name[:-5] + ".md"
                    (markdown_dir / markdown_name).write_text(
                        assistant_text.rstrip() + "\n", encoding="utf-8"
                    )
                completed += 1
                print(f"[{position}/{len(jobs)}] success {output_name}")
            else:
                if (
                    args.output_format == "markdown"
                    and assistant_text is not None
                    and assistant_text.strip()
                ):
                    markdown_name = output_name[:-5] + ".md"
                    (partial_markdown_dir / markdown_name).write_text(
                        assistant_text.rstrip() + "\n", encoding="utf-8"
                    )
                failed += 1
                print(
                    f"[{position}/{len(jobs)}] invalid-response {output_name}: {parse_error}",
                    file=sys.stderr,
                )
        except Exception as exc:
            record.update(
                {
                    "status": "failed",
                    "finished_at_utc": utc_now(),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
            failed += 1
            print(f"[{position}/{len(jobs)}] failed {output_name}: {exc}", file=sys.stderr)
        output_path.write_text(
            json.dumps(record, indent=2, ensure_ascii=False, allow_nan=False),
            encoding="utf-8",
        )

    print(f"Completed: {completed}; skipped: {skipped}; failed: {failed}")
    print(f"Run directory: {run_dir}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
