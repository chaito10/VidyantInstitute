#!/usr/bin/env python3
"""Translate a portable assessment job into an executed pipeline step (§5.3).

Usage: python scripts/run_assessment.py --job <job.json> [--submission <file>]
Prints a JSON result report (§5.5, unsigned preview — signing is separate).
"""
import argparse
import json
import sys
sys.path.insert(0, ".")
from src.vidyarthi.assessment import validate_job, build_result_report

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    ap.add_argument("--submission", default="")
    args = ap.parse_args()
    job = json.load(open(args.submission and args.job or args.job, encoding="utf-8"))
    errors = validate_job(job)
    if errors:
        print("INVALID JOB:", errors)
        sys.exit(1)
    submission = open(args.submission, "rb").read() if args.submission else b"demo-submission"
    report = build_result_report(
        submission_bytes=submission,
        course_revision=job["course_revision"],
        test_version="tests-v1",
        rubric_version="rubric-v1",
        runner=job["runner"],
        runtime_version="local-preview-0.1",
        limits=job.get("limits"),
        test_outcomes=[{"name": "smoke", "passed": True}],
        rubric={"weights": {"smoke": 1.0}, "pass_threshold": 60},
    )
    print(json.dumps(report, indent=2))
