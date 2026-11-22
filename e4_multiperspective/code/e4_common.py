"""E4 helpers kept inside the E4 folder (the shared package src/pcr is not modified until
pipeline v2 is frozen)."""
from __future__ import annotations

import gzip
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))
from pcr.logs import _local, is_technical_activity  # noqa: E402

E4_ROOT = Path(__file__).resolve().parents[1]
E4_RESULTS = E4_ROOT / "results"


def read_mxml_events(path: Path) -> list[list[tuple[str, str]]]:
    """Like read_mxml, but every event is (activity, ISO timestamp string), in file order.
    The same events are kept as in read_mxml (completed, non-technical), so the activity
    sequences of both readers are identical."""
    traces: list[list[tuple[str, str]]] = []
    with gzip.open(path, "rb") as stream:
        for _, elem in ET.iterparse(stream, events=("end",)):
            if _local(elem.tag) != "ProcessInstance":
                continue
            events = []
            for entry in elem:
                if _local(entry.tag) != "AuditTrailEntry":
                    continue
                fields = {_local(child.tag): (child.text or "").strip() for child in entry}
                name = fields.get("WorkflowModelElement")
                if fields.get("EventType", "complete") == "complete" and name and not is_technical_activity(name):
                    events.append((name, fields.get("timestamp", "")))
            traces.append(events)
            elem.clear()
    return traces


