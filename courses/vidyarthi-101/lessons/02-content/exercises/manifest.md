# Exercise — validate and break a manifest

1. Run `python scripts/validate_course.py courses/vidyarthi-101` (expect VALID).
2. Copy `course.json` to a temp dir, delete the `language` field, re-run validation
   against the copy (expect an error naming the missing field).
3. Restore and change `credits.value` to 999 — confirm validation still passes,
   and explain why (§3.3: descriptive metadata, not entitlement).
