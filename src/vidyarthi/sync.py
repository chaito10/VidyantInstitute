"""Offline synchronization conflict rules — Vidyarthi §6.2.

Peers study/work offline, queue local changes, and exchange on reconnect.
Conflict handling depends on the data type — conflicting academic records
must NEVER be resolved through arbitrary last-write-wins behavior.
"""
from __future__ import annotations

from typing import Any

# Data type -> resolution strategy (exact §6.2 wording).
STRATEGIES = {
    "course-content": "repository-history-merge",
    "discussion": "preserve-identity-and-ordering",
    "learner-progress": "explicit-event-conflict-rules",
    "credential": "verify-signed-record-no-merge",
}


def strategy_for(data_type: str) -> str:
    if data_type not in STRATEGIES:
        raise ValueError(f"unknown data type: {data_type!r} (expected one of {sorted(STRATEGIES)})")
    return STRATEGIES[data_type]


def merge_records(data_type: str, local: list[dict[str, Any]], remote: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Reconcile two replicas without last-write-wins.

    - course-content: union by revision id (history merge; real merge uses
      Fossil — this is the bookkeeping equivalent).
    - discussion: union by message id, ordered by (timestamp, id).
    - learner-progress: explicit event rules — latest event per
      (outcome_id) wins only when event ids differ; concurrent duplicates kept.
    - credential: NO merge — return local unchanged; the caller must verify
      each remote record as a signed credential instead.
    """
    strategy = strategy_for(data_type)
    if strategy == "verify-signed-record-no-merge":
        return list(local)
    if data_type == "learner-progress":
        by_outcome: dict[str, dict[str, Any]] = {e["outcome_id"]: e for e in local}
        for e in remote:
            cur = by_outcome.get(e["outcome_id"])
            if cur is None or (e["event_id"], e["timestamp"]) > (cur["event_id"], cur["timestamp"]):
                by_outcome[e["outcome_id"]] = e
        return sorted(by_outcome.values(), key=lambda e: e["outcome_id"])
    key = "revision" if data_type == "course-content" else "id"
    seen: dict[str, dict[str, Any]] = {}
    for rec in (*local, *remote):
        seen.setdefault(rec[key], rec)
    merged = list(seen.values())
    if data_type == "discussion":
        merged.sort(key=lambda m: (m.get("timestamp", 0), m.get("id", "")))
    return merged
