# Lesson 2 — Courses as versioned artifacts

Outcome: `course-packages` (syllabus outcome 2). Spec: §3.

## A course is a package, not a database row

A course repository holds the syllabus, outcomes, notes, slides, assessments,
exercises, references, projects, and media — in **Markdown and JSON**, readable
without proprietary tooling. **Fossil SCM** provides history: inspection,
branches, sync, and pinning evidence to specific revisions.

## Reference layout (§3.2)

```text
course/
├── course.json  syllabus.md  prerequisites.md  manifest.json
├── lessons/01-foundations/{lesson.md, slides.md, quiz.json, exercises/, assets/}
├── assessments/{rubric.json, tests/, project.md}
└── projects/ papers/ discussions/ references/ media/
```

## Manifest (§3.3)

Required: `schema_version`, unique `id` (`vidyarthi:<subject>:<number>`),
`title`, semver `version`, `language`. Also: level, prerequisites, outcomes,
modules (`id` + `path`), assessment criteria, deps, **license**, hashes,
credential mappings.

> `credits` is **descriptive metadata only** — it never auto-creates an
> academic entitlement. An authorized issuer evaluates it under a published
> policy (§8).

## Lifecycle (§3.4)

Fork → define outcomes/assessments → AI drafts → automated checks → educator
review → **pinned release** → learners use that revision. Later edits create
**new revisions**; forks preserve attribution. Validate any package with:

```bash
python scripts/validate_course.py <course-dir>
```
