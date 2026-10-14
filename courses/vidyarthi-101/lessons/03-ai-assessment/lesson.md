# Lesson 3 — BYOK AI and Pipelight assessment

Outcomes: `ai-assessment` (syllabus outcomes 3–4). Spec: §4–§5.

## Bring Your Own Key (§4.1–§4.2)

No centrally funded provider. Configure hosted APIs, OpenAI-compatible
endpoints, **Ollama / llama.cpp**, institutional gateways, or community
adapters. Capabilities (streaming, tools, multimodal) are **optional**.

Key rules: keys live **in memory** by default; persist only on explicit opt-in
with encryption. **Never** in repos, peers, assets, or logs. Disclose local vs
remote inference. Never silently proxy keys through a shared backend
(see `src/vidyarthi/byok.py`, `public/vidyarthi.html` §3).

## Generation pipeline (§4.3)

Plan → lessons → **Marp slides** (shared outcome IDs) → quizzes/rubrics →
media scripts → **validation** → human review → pinned release. Drafts stay
drafts until checks pass — and checks ≠ correctness.

## Tutor (§4.4)

Course-grounded, cites source lessons, hints before solutions, never invents
citations. Adaptive recommendations are explainable and overridable; profiles
stay learner-local.

## Pipelight assessment (§5)

Portable job schema (`schemas/assessment-job.schema.json`) → adapter →
pipeline: validate manifest/hashes → validate definition → **restricted job**
(no network; capped time/memory) → deterministic tests → evidence → **rubric**
→ report → **authorized signing** → record/sync.

Trust split: runners prove tests passed — **not** authorship, rubric validity,
or degree worth. Reports record hashes, revisions, runner/runtime, limits,
outcomes, score/rationale, signer, timestamp (§5.5).
