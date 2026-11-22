#!/usr/bin/env python3
"""Run an IEEE Access API manifest with hash validation and safe resume."""

from __future__ import annotations

import argparse
import csv
import hashlib
import http.client
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "Code"))
from run_glm_experiment import build_request, extract_prompt_sections, parse_assistant_text  # noqa: E402


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def post_json_fresh(
    endpoint: str,
    api_key: str,
    payload: dict,
    user_agent: str,
    timeout: int,
    max_retries: int,
) -> dict:
    """POST JSON using a brand-new connection for every attempt.

    The shared urllib runner intermittently raised ``EBADF`` on macOS before
    receiving an HTTP response.  An explicit short-lived connection avoids
    reusing any stale descriptor while preserving the same API contract.
    """
    parsed = urlsplit(endpoint)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError(f"Invalid API endpoint: {endpoint}")
    path = parsed.path or "/"
    if parsed.query:
        path = f"{path}?{parsed.query}"
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Language": "en-US,en",
        "User-Agent": user_agent,
        "Connection": "close",
    }
    transient = {408, 409, 429, 500, 502, 503, 504}
    errors: list[str] = []
    for attempt in range(max_retries + 1):
        connection_class = (
            http.client.HTTPSConnection if parsed.scheme == "https"
            else http.client.HTTPConnection
        )
        connection = connection_class(parsed.hostname, parsed.port, timeout=timeout)
        try:
            connection.request("POST", path, body=body, headers=headers)
            response = connection.getresponse()
            response_body = response.read().decode("utf-8", errors="replace")
            if 200 <= response.status < 300:
                return json.loads(response_body)
            error = f"HTTP {response.status}: {response_body}"
            errors.append(f"attempt {attempt + 1}: {error}")
            if response.status not in transient:
                raise RuntimeError(error)
        except (OSError, TimeoutError, http.client.HTTPException, json.JSONDecodeError) as exc:
            errors.append(f"attempt {attempt + 1}: {type(exc).__name__}: {exc}")
        finally:
            connection.close()
        if attempt < max_retries:
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError("Request failed after retries; " + " | ".join(errors))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--endpoint", default="https://api.int2.net/v1/chat/completions")
    parser.add_argument("--max-tokens", type=int, default=0, help="0 omits the request cap")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--conditions", nargs="*")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-resume", action="store_true")
    args = parser.parse_args()

    manifest = args.manifest.resolve()
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"run_id", "case_id", "condition", "prompt_path", "prompt_hash",
                "evidence_path", "evidence_hash", "model", "temperature", "top_p"}
    missing = required - set(rows[0]) if rows else required
    if missing:
        raise SystemExit(f"Manifest missing columns: {sorted(missing)}")
    if args.conditions:
        allowed = set(args.conditions)
        rows = [row for row in rows if row["condition"] in allowed]
    rows.sort(key=lambda row: (row["condition"], row["case_id"]))
    if args.limit is not None:
        rows = rows[:args.limit]

    run_dir = args.run_dir.resolve()
    response_dir, markdown_dir = run_dir / "responses", run_dir / "markdown"
    response_dir.mkdir(parents=True, exist_ok=True)
    markdown_dir.mkdir(parents=True, exist_ok=True)
    api_key = os.environ.get("GLM_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("GLM_API_KEY is not set")

    completed = skipped = failed = 0
    for index, row in enumerate(rows, 1):
        prompt_path = ROOT / row["prompt_path"]
        evidence_path = ROOT / row["evidence_path"]
        prompt_bytes, evidence_bytes = prompt_path.read_bytes(), evidence_path.read_bytes()
        if sha256_bytes(prompt_bytes) != row["prompt_hash"]:
            raise SystemExit(f"Prompt hash mismatch: {prompt_path}")
        if sha256_bytes(evidence_bytes) != row["evidence_hash"]:
            raise SystemExit(f"Evidence hash mismatch: {evidence_path}")
        evidence = json.loads(evidence_bytes)
        if evidence.get("case", {}).get("case_id") != row["case_id"]:
            raise SystemExit(f"Case mismatch: {evidence_path}")
        system, template = extract_prompt_sections(prompt_path)
        evidence_text = evidence_bytes.decode("utf-8")
        user = template.replace("{{EVIDENCE_JSON}}", evidence_text)
        config = {
            "model": row["model"], "temperature": float(row["temperature"]),
            "top_p": float(row["top_p"]), "thinking": {"type": "disabled"},
            "stream": False, "max_tokens": args.max_tokens,
        }
        if not args.max_tokens:
            config["max_tokens"] = None
        payload = build_request(config, system, user, "markdown")
        if payload.get("max_tokens") is None:
            payload.pop("max_tokens", None)
        name = f"{row['case_id']}__{row['condition']}"
        output_path, md_path = response_dir / f"{name}.json", markdown_dir / f"{name}.md"
        if output_path.exists() and not args.no_resume:
            previous = json.loads(output_path.read_text(encoding="utf-8"))
            if previous.get("status") == "success_complete":
                skipped += 1
                print(f"[{index}/{len(rows)}] skip {name}")
                continue
        if args.dry_run:
            print(f"[{index}/{len(rows)}] valid {name}: evidence={len(evidence.get('evidence', []))}")
            completed += 1
            continue
        started = now()
        try:
            response = post_json_fresh(
                args.endpoint, api_key or "", payload,
                "IEEE-Access-Process-Drift/1.0", args.timeout, args.max_retries,
            )
            text, parse_error = parse_assistant_text(response)
            choice = (response.get("choices") or [{}])[0]
            status = "success_complete" if text and not parse_error else "invalid_response"
            record = {
                "run_id": row["run_id"], "paper_scope": row.get("paper_scope", "IEEE_ACCESS"),
                "case_id": row["case_id"], "condition": row["condition"],
                "manifest_path": str(args.manifest), "evidence_hash": row["evidence_hash"],
                "prompt_hash": row["prompt_hash"], "model": row["model"],
                "started_at_utc": started, "finished_at_utc": now(), "status": status,
                "finish_reason": choice.get("finish_reason"), "usage": response.get("usage", {}),
                "visible_text": text, "parse_error": parse_error, "raw_response": response,
            }
            output_path.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
            if text:
                md_path.write_text(text, encoding="utf-8")
            completed += status == "success_complete"
            failed += status != "success_complete"
            print(f"[{index}/{len(rows)}] {status} {name}")
        except Exception as exc:
            failed += 1
            output_path.write_text(json.dumps({"status": "failed", "case_id": row["case_id"],
                                                "condition": row["condition"], "error": str(exc),
                                                "started_at_utc": started, "finished_at_utc": now()},
                                               ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"[{index}/{len(rows)}] failed {name}: {exc}", file=sys.stderr)
    print(f"completed={completed} skipped={skipped} failed={failed} jobs={len(rows)}")


if __name__ == "__main__":
    main()
