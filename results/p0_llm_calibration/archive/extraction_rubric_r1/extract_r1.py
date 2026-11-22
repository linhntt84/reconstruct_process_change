"""Blind structured extraction with Claude through the headless Claude Code CLI.

Runs ``claude -p`` under the user's claude.ai subscription: no tools, no MCP servers,
no slash commands, no session persistence, in an empty working directory, with the
rubric as the whole system prompt and a JSON schema for the answer. The explanation text
is the only input; case identifiers, references and model names are never passed.

Usage limits: when the CLI reports a usage/rate limit, ``UsageLimitReached`` is raised
so the caller can wait for the reset. Nothing here enables or uses extra (overage) usage.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .paths import ROOT

MODEL = "claude-opus-5-5"
RUBRIC = ROOT / "prompts" / "EXTRACTION_RUBRIC_V2_EN.md"
ACTIVITY = {"type": "array", "items": {"type": "string", "pattern": "^A[0-9]{2,3}$"}}
MECHANISMS = ["fragment_added", "fragment_removed", "fragment_moved", "fragments_swapped",
              "fragment_substituted", "choice_to_sequence", "sequence_to_choice", "parallel_to_sequence",
              "sequence_to_parallel", "became_repeated", "stopped_repeating", "became_optional",
              "became_mandatory", "branch_frequency_changed", "timing_changed",
              "resource_allocation_changed", "handover_changed", "other", "none"]
PATTERNS = ["SerialRemoval", "ParallelRemoval", "ConditionalRemoval", "Substitute", "Swap", "SerialMove",
            "ConditionalMove", "ParallelMove", "ConditionalToSequence", "ParallelToSequence", "Loop", "Skip",
            "Frequency", "none"]
PATTERN_FIELD = """
pattern
  The benchmark change pattern that the hypothesis corresponds to, as one of:
  SerialRemoval (fragment added or removed within a sequence), ParallelRemoval (added or
  removed as a parallel branch), ConditionalRemoval (added or removed as a choice branch),
  Substitute (fragment replaced by another), Swap (two fragments exchange order),
  SerialMove (fragment moved to another sequential position), ConditionalMove (moved into
  or out of a choice), ParallelMove (moved into or out of a parallel region),
  ConditionalToSequence (choice becomes sequence or the reverse), ParallelToSequence
  (parallel becomes sequence or the reverse), Loop (fragment becomes or stops being
  repeated), Skip (fragment becomes optional or mandatory again), Frequency (structure
  unchanged, only branch frequencies change), or "none" (no hypothesis).
"""
LIMIT_MARKERS = re.compile(r"usage limit|limit reached|hit your limit|rate.?limit|out of (extra )?usage|"
                           r"quota|429|overloaded", re.I)


class UsageLimitReached(RuntimeError):
    def __init__(self, message: str, reset_epoch: int | None = None):
        super().__init__(message)
        self.reset_epoch = reset_epoch


def schema(variant: str) -> dict[str, Any]:
    properties = {
        "support_level": {"type": "string", "enum": ["insufficient", "weak", "supported", "unparsed"]},
        "central_activities": ACTIVITY, "context_activities": ACTIVITY,
        "mechanism": {"type": "string", "enum": MECHANISMS},
        "perspectives": {"type": "array", "items": {"type": "string", "enum": ["control_flow", "time", "resource"]}},
        "note": {"type": "string"},
    }
    if variant == "main":
        properties["pattern"] = {"type": "string", "enum": PATTERNS}
    return {"type": "object", "properties": properties, "required": list(properties),
            "additionalProperties": False}


def system_prompt(variant: str) -> str:
    text = RUBRIC.read_text(encoding="utf-8").split("\n", 2)[2]  # drop the title line
    return text.replace("{{PATTERN_FIELD}}", PATTERN_FIELD if variant == "main" else "")


def claude_binary() -> str:
    return os.environ.get("CLAUDE_CODE_EXECPATH") or "claude"


def extract(explanation: str, variant: str = "main", model: str = MODEL, timeout: int = 600) -> dict[str, Any]:
    prompt_text = system_prompt(variant)
    schema_text = json.dumps(schema(variant))
    with tempfile.TemporaryDirectory(prefix="pcr_extract_") as workdir:
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
    return {"extraction": output, "variant": variant, "model": model,
            "rubric_sha256": hashlib.sha256(prompt_text.encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema_text.encode()).hexdigest(),
            "started_at_utc": started, "latency_seconds": latency,
            "cli_version": cli_version(), "usage": envelope.get("usage"),
            "total_cost_usd_reported": envelope.get("total_cost_usd"),
            "session_model_usage": envelope.get("modelUsage")}


_VERSION: str | None = None


def cli_version() -> str:
    global _VERSION
    if _VERSION is None:
        _VERSION = subprocess.run([claude_binary(), "--version"], capture_output=True, text=True).stdout.strip()
    return _VERSION
