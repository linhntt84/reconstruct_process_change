"""Event-log readers and window anonymization.

`neutralize_windows` and the technical-marker rule are copied from the code used
for the submitted manuscript, so anonymous labels (A01, A02, ...) are identical.
Size-3 Ostovar MXML logs read here match the cdrift-evaluation XES logs used in
the paper trace by trace (2999/2999).
"""
from __future__ import annotations

import gzip
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

TECHNICAL_ACTIVITY_PREFIXES = ("DRIFT_",)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def is_technical_activity(value: Any) -> bool:
    return isinstance(value, str) and value.startswith(TECHNICAL_ACTIVITY_PREFIXES)


def read_mxml(path: Path) -> list[list[str]]:
    """Return the completed-activity sequence of every process instance, in file order."""
    traces: list[list[str]] = []
    with gzip.open(path, "rb") as stream:
        for _, elem in ET.iterparse(stream, events=("end",)):
            if _local(elem.tag) != "ProcessInstance":
                continue
            sequence = []
            for entry in elem:
                if _local(entry.tag) != "AuditTrailEntry":
                    continue
                fields = {_local(child.tag): (child.text or "").strip() for child in entry}
                name = fields.get("WorkflowModelElement")
                if fields.get("EventType", "complete") == "complete" and name and not is_technical_activity(name):
                    sequence.append(name)
            traces.append(sequence)
            elem.clear()
    return traces


def neutralize_windows(
    before: list[dict[str, Any]], after: list[dict[str, Any]], enabled: bool = True
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, str]]:
    """Map activity labels to A01, A02, ... in sorted order over both windows."""
    labels = sorted({str(a) for trace in before + after for a in trace["activities"]})
    mapping = {label: f"A{index:02d}" for index, label in enumerate(labels, 1)}
    if not enabled:
        mapping = {label: label for label in labels}

    def convert(traces: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return [{"activities": [mapping[str(a)] for a in trace["activities"]]} for trace in traces]

    return convert(before), convert(after), mapping
