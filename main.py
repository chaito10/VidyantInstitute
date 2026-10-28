#!/usr/bin/env python3
"""Vidyarthi entrypoint — local-first micro-learning university core (v0.3).

Usage:
    python main.py validate [course_dir]   validate a course package
    python main.py info                    print spec version
"""
import sys

from src.vidyarthi import SPEC_VERSION


def main(argv: list[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "info"
    if cmd == "info":
        print(f"Vidyarthi core ({SPEC_VERSION})")
        return 0
    if cmd == "validate":
        from src.vidyarthi.course import validate_course_dir
        target = argv[2] if len(argv) > 2 else "courses/cybersecurity-101"
        errors = validate_course_dir(target)
        if errors:
            print("INVALID:")
            for e in errors:
                print(f" - {e}")
            return 1
        print(f"VALID: {target}")
        return 0
    print(f"unknown command: {cmd!r} (expected 'info' or 'validate')")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
