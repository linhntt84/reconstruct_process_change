"""Blind extraction for E4 with rubric r4 (r3 + time_activities, time_direction).

Same mechanism as pcr.extract (claude -p, no tools, no MCP, empty working directory, JSON
schema, usage-limit handling), with the E4 rubric and schema; pcr.extract is not modified.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from e4_common import REPO  # noqa: F401  (puts src/ on sys.path)
from pcr.extract import (ACTIVITY, LIMIT_MARKERS, MODEL, PATTERN_FIELD, UsageLimitReached, claude_binary,
                         cli_version, schema as base_schema)

RUBRIC_R4 = Path(__file__).resolve().parent / "EXTRACTION_RUBRIC_E4_R4_EN.md"


def schema_r4(variant: str = "main") -> dict[str, Any]:
    s = base_schema(variant)
    s["properties"]["time_activities"] = ACTIVITY
    s["properties"]["time_direction"] = {"type": "string", "enum": ["increase", "decrease", "mixed", "none"]}
    s["required"] = list(s["properties"])
    return s


def system_prompt_r4(variant: str = "main") -> str:
    text = RUBRIC_R4.read_text(encoding="utf-8").split("\n", 2)[2]
    main = variant == "main"
    return (text.replace("{{PATTERN_FIELD}}", PATTERN_FIELD if main else "")
            .replace("{{ALTERNATIVE_PATTERN_NAME}}", ", alternative_pattern" if main else "")
            .replace("{{ALTERNATIVE_PATTERN_HINT}}", " and the pattern it corresponds to" if main else "")
            .replace("{{ALTERNATIVE_PATTERN_NONE}}", ", with alternative_pattern \"none\"" if main else ""))


def extract_r4(explanation: str, variant: str = "main", model: str = MODEL, timeout: int = 600) -> dict[str, Any]:
    prompt_text = system_prompt_r4(variant)
    schema_text = json.dumps(schema_r4(variant))
    with tempfile.TemporaryDirectory(prefix="pcr_extract_e4_") as workdir:
        prompt_file = Path(workdir) / "system.md"
        prompt_file.write_text(prompt_text, encoding="utf-8")
        command = [claude_binary(), "-p", "--model", model, "--system-prompt-file", str(prompt_file),
                   "--tools", "", "--strict-mcp-config", "--disable-slash-commands",
                   "--no-session-persistence", "--output-format", "json", "--json-schema", schema_text]
        started, t0 = datetime.now(timezone.utc).isoformat(), time.perf_counter()
        proc = subprocess.run(command, input="Explanation to record:\n\n" + explanation, text=True,
                              capture_output=True, cwd=workdir, timeout=timeout)
    latency = round(time.perf_counter() - t0, 2)
    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        envelope = {"is_error": True, "result": (proc.stdout or "") + (proc.stderr or "")}
    message = str(envelope.get("result", "")) + " " + (proc.stderr or "")
    if envelope.get("is_error") or proc.returncode != 0:
        if LIMIT_MARKERS.search(message):
            reset = re.search(r"\|(\d{10})", message)
            raise UsageLimitReached(message.strip()[:300], int(reset.group(1)) if reset else None)
        raise RuntimeError(f"claude exited {proc.returncode}: {message.strip()[:500]}")
    output = envelope.get("structured_output")
    if output is None:
        output = json.loads(envelope.get("result") or "{}")
    return {"extraction": output, "variant": variant, "model": model, "rubric": "r4-e4",
            "rubric_sha256": hashlib.sha256(prompt_text.encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema_text.encode()).hexdigest(),
            "started_at_utc": started, "latency_seconds": latency, "cli_version": cli_version(),
            "usage": envelope.get("usage")}


RUBRIC_R5 = Path(__file__).resolve().parent / "EXTRACTION_RUBRIC_E4_R5_EN.md"


def extract_r5(explanation: str, model: str = MODEL, timeout: int = 600) -> dict[str, Any]:
    """Rubric r5 = r4 + resource_activities (E4b)."""
    global RUBRIC_R4
    saved_rubric, saved_schema = RUBRIC_R4, globals()["schema_r4"]

    def schema_r5(variant: str = "main") -> dict[str, Any]:
        s = saved_schema(variant)
        s["properties"]["resource_activities"] = ACTIVITY
        s["required"] = list(s["properties"])
        return s
    RUBRIC_R4, globals()["schema_r4"] = RUBRIC_R5, schema_r5
    try:
        result = extract_r4(explanation, "main", model, timeout)
    finally:
        RUBRIC_R4, globals()["schema_r4"] = saved_rubric, saved_schema
    result["rubric"] = "r5-e4"
    return result
