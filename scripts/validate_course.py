#!/usr/bin/env python3
"""Validate a Vidyarthi course directory (§3). Exit 0 = valid, 1 = invalid."""
import sys
sys.path.insert(0, ".")
from src.vidyarthi.course import validate_course_dir

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "courses/cybersecurity-101"
    errors = validate_course_dir(target)
    if errors:
        print("INVALID:")
        for e in errors:
            print(f" - {e}")
        sys.exit(1)
    print(f"VALID: {target}")
