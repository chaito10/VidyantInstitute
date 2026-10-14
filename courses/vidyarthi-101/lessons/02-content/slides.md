---
marp: true
paginate: true
title: Vidyarthi 101 — Versioned courses
---

## Courses as versioned artifacts (§3)

Packages, not database rows. Markdown + JSON. Fossil history.

---

## Manifest essentials

`schema_version` · `id` (`vidyarthi:<subject>:<number>`) · `title` ·
semver `version` · `language` · outcomes · modules · license · hashes

Credits = descriptive metadata. Never auto-entitlements.

---

## Lifecycle

Fork → outcomes → AI drafts → checks → review → **pinned release** →
study that revision. New edits = new revisions.

Validate: `python scripts/validate_course.py <course-dir>`
