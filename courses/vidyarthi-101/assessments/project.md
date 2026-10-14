# Capstone project — publish your own micro-course

Build a micro-course package that documents a topic you know, following the
§3.2 reference layout used by this course:

```text
course/
├── course.json  syllabus.md  prerequisites.md
├── lessons/<module>/{lesson.md, slides.md, quiz.json, exercises/}
└── assessments/{rubric.json, tests/, project.md}
```

## Requirements

1. `course.json` validates: `python scripts/validate_course.py <your-course-dir>`
   (valid `schema_version`, `id` matching `vidyarthi:<subject>:<number>`,
   semver `version`, `language`, one module per lesson directory).
2. At least two lessons, each with `lesson.md`, Marp-compatible `slides.md`,
   and a `quiz.json` with answer keys + explanations.
3. `assessments/rubric.json` with per-module weights and a pass threshold;
   `assessments/project.md` describing a practical artifact.
4. Credits listed as descriptive metadata with a named system — no claim of
   entitlement (§3.3, §8.3).
5. Human review: a reviewer checks factual correctness and outcome coverage
   before the package is pinned as a release (§3.4, §4.3 Stage 7).

## Grading

Rubric-weighted quiz/test evidence plus reviewer sign-off. Passing the
automated checks alone does not establish correctness or academic suitability
(§4.3, §5.2).
