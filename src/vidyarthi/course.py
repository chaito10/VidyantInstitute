"""Course manifest validation — Vidyarthi §3.

A course is a version-controlled academic package (Fossil SCM), not a bare
database record. Reference layout (§3.2)::

    course/
    ├── course.json
    ├── syllabus.md
    ├── prerequisites.md
    ├── manifest.json
    ├── lessons/01-foundations/{lesson.md,slides.md,quiz.json,exercises/,assets/}
    ├── assessments/{rubric.json,tests/,project.md}
    ├── projects/ papers/ discussions/ references/ media/

Mandatory course.json fields (§3.3): schema_version, id, title, version,
language. Optional: level, credits (descriptive only — §3.3: must not
automatically create an academic entitlement), outcomes, modules,
assessment, license, hashes.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
COURSE_ID_RE = re.compile(r"^vidyarthi:[a-z0-9-]+:[a-z0-9-]+$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")

REQUIRED_FIELDS = ("schema_version", "id", "title", "version", "language")
OPTIONAL_DIRS = (
    "lessons", "assessments", "projects", "papers",
    "discussions", "references", "media",
)


def validate_course_manifest(data: dict[str, Any]) -> list[str]:
    """Return a list of validation errors (empty = valid)."""
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if not data.get(field):
            errors.append(f"missing required field: {field}")
    if data.get("schema_version") and data["schema_version"] != SCHEMA_VERSION:
        errors.append(f"unsupported schema_version: {data.get('schema_version')!r} (expected {SCHEMA_VERSION!r})")
    if data.get("id") and not COURSE_ID_RE.match(data["id"]):
        errors.append(f"invalid id format: {data.get('id')!r} (expected 'vidyarthi:<subject>:<number>')")
    if data.get("version") and not SEMVER_RE.match(str(data["version"])):
        errors.append(f"invalid version (expected semver): {data.get('version')!r}")
    # credits are descriptive metadata only (§3.3)
    credits = data.get("credits")
    if credits is not None:
        if not isinstance(credits, dict) or "value" not in credits or "system" not in credits:
            errors.append("credits must be an object with 'value' and 'system' (descriptive only, not an entitlement)")
    for mod in data.get("modules", []) or []:
        if not isinstance(mod, dict) or not mod.get("id") or not mod.get("path"):
            errors.append(f"module must have 'id' and 'path': {mod!r}")
    return errors


def load_course_json(path: str | Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_course_dir(course_dir: str | Path) -> list[str]:
    """Validate a course directory on disk. Returns error list."""
    course_dir = Path(course_dir)
    errors: list[str] = []
    manifest = course_dir / "course.json"
    if not manifest.exists():
        return [f"missing course.json in {course_dir}"]
    try:
        data = load_course_json(manifest)
    except Exception as e:
        return [f"course.json is not valid JSON: {e}"]
    errors.extend(validate_course_manifest(data))
    for mod in data.get("modules", []) or []:
        mod_path = course_dir / str(mod.get("path", ""))
        if not mod_path.exists():
            errors.append(f"module path missing on disk: {mod.get('path')}")
    return errors


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
