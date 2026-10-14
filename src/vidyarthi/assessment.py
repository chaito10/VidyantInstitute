"""Assessment job / result handling — Vidyarthi §5.

Pipelight provides the CI workflow; this module defines the portable
application-level schema (NOT a native Pipelight config file — an adapter
translates it into executable pipeline steps, §5.3).

Workflow (§5.2): manifest+hash validation → assessment-definition validation
→ restricted job → deterministic tests → evidence → rubric → report →
authorized signing → record/sync.

Trust separation (§5.2): a test runner establishes that tests passed; it
cannot establish authorship, rubric validity, or degree entitlement.
WASM alone is not a complete sandbox (§5.5): resource limits + denied
network/fs are mandatory.
"""
from __future__ import annotations

import hashlib
import json
import time
from typing import Any

SCHEMA_VERSION = "1.0"
VALID_RUNNERS = ("wasm", "rust-restricted", "isolated")
REQUIRED_JOB_FIELDS = (
    "schema_version", "job_id", "course_id",
    "course_revision", "submission_id", "runner", "tests",
)
REQUIRED_REPORT_FIELDS = (
    "submission_hash", "course_revision", "test_version",
    "rubric_version", "runner", "runtime_version",
    "limits", "test_outcomes", "score",
    "grading_rationale", "signing_identity", "timestamp",
)

DEFAULT_LIMITS = {"timeout_seconds": 30, "memory_mb": 128, "network": False}


def validate_job(job: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_JOB_FIELDS:
        if job.get(field) in (None, "", []):
            errors.append(f"missing required field: {field}")
    if job.get("schema_version") and job["schema_version"] != SCHEMA_VERSION:
        errors.append(f"unsupported schema_version: {job.get('schema_version')!r}")
    if job.get("runner") and job["runner"] not in VALID_RUNNERS:
        errors.append(f"unsupported runner: {job.get('runner')!r} (expected one of {VALID_RUNNERS})")
    limits = job.get("limits") or {}
    if limits.get("network", False) is not False:
        errors.append("default assessment jobs must deny network access (limits.network=false, §5.5)")
    return errors


def apply_rubric(test_outcomes: list[dict[str, Any]], rubric: dict[str, Any]) -> tuple[float, str]:
    """Apply a published rubric to test outcomes.

    Returns (score 0-100, rationale). Rubric format::

        {"weights": {"test-id": weight, ...}, "pass_threshold": 60}
    """
    weights = (rubric or {}).get("weights", {}) or {}
    total = sum(weights.values()) or 1.0
    earned = 0.0
    details: list[str] = []
    for t in test_outcomes:
        name = t.get("name", "?")
        passed = bool(t.get("passed"))
        w = float(weights.get(name, 1.0))
        if passed:
            earned += w
        details.append(f"{name}: {'pass' if passed else 'fail'} (weight {w})")
    score = round(100.0 * earned / total, 2)
    threshold = (rubric or {}).get("pass_threshold", 60)
    verdict = "PASS" if score >= threshold else "FAIL"
    rationale = f"{verdict} — score {score} vs threshold {threshold}; " + "; ".join(details)
    return score, rationale


def build_result_report(
    *,
    submission_bytes: bytes,
    course_revision: str,
    test_version: str,
    rubric_version: str,
    runner: str,
    runtime_version: str,
    limits: dict[str, Any] | None,
    test_outcomes: list[dict[str, Any]],
    rubric: dict[str, Any] | None = None,
    signing_identity: str = "unauthorized-local-preview",
) -> dict[str, Any]:
    """Build a §5.5 assessment report (unsigned; see credentials.sign_credential)."""
    score, rationale = apply_rubric(test_outcomes, rubric or {})
    return {
        "submission_hash": hashlib.sha256(submission_bytes).hexdigest(),
        "course_revision": course_revision,
        "test_version": test_version,
        "rubric_version": rubric_version,
        "runner": runner,
        "runtime_version": runtime_version,
        "limits": limits or dict(DEFAULT_LIMITS),
        "test_outcomes": test_outcomes,
        "score": score,
        "grading_rationale": rationale,
        "signing_identity": signing_identity,
        "timestamp": int(time.time()),
    }


def validate_report(report: dict[str, Any]) -> list[str]:
    return [f"missing required field: {f}" for f in REQUIRED_REPORT_FIELDS if report.get(f) is None]
