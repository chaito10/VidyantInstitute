# Vidyarthi — Digital Distributed University

Vidyarthi is a **peer-to-peer, AI-driven micro-learning university**: version-controlled
course repositories, a minimal offline-capable web client, automated assessment pipelines,
user-controlled AI providers, peer networking, gamification, and cryptographically
verifiable credentials. **Local-first, not unconditionally decentralized.**

Full spec: [docs/DECISIONS.md](docs/DECISIONS.md) (consolidated decision log).
White paper: [white_paper.md](white_paper.md) (architectural proposal).

## Quick start

```bash
# Clone
git clone https://github.com/charudatta10/VidyantInstitute.git
cd VidyantInstitute

# Validate a sample course
python scripts/validate_course.py courses/cybersecurity-101

# Open the offline client in a browser
# public/vidyarthi.html  (load course.json + quiz.json from a sample course)

# Run an assessment job
python scripts/run_assessment.py --job courses/cybersecurity-101/assessments/tests/basic.json

# Run tests
python -m pytest tests/ -q
```

## Architecture — six logical layers

| Layer | Responsibility | Technology |
| --- | --- | --- |
| Learning interface | Lessons, quizzes, dashboards, offline | HTML5, vanilla JS, CSS |
| Academic content | Course packages, history, projects, references | Fossil SCM, Markdown, JSON |
| Application coordination | Accounts, discovery, sync metadata (NOT canonical authority) | PocketBase |
| AI assistance | Tutoring, generation, feedback | BYOK adapters + local endpoints |
| Execution & assessment | Validation, test execution, scoring | Pipelight, Rust, WASM |
| Distribution & trust | Peer sync, signed results, credentials | Fossil sync, optional libp2p, Ed25519 |

Deployment profiles: **A** personal (browser + local repos + optional local AI) →
**B** community (+ PocketBase, P2P sync, assessment jobs) → **C** institutional
(+ authorized assessors, issuer keys). All share course/credential formats.

## Project structure

| Path | Contents |
| --- | --- |
| `white_paper.md` | Architectural proposal (§1–15) |
| `docs/DECISIONS.md` | Consolidated decision log + open questions |
| `src/vidyarthi/` | `course`, `assessment`, `credentials`, `byok`, `gamification`, `sync` |
| `schemas/` | Course, assessment-job, assessment-result, credential JSON schemas |
| `courses/` | Sample Fossil-ready course packages |
| `public/vidyarthi.html` | Single-file offline learning client |
| `pipelight/` + `scripts/` | CI pipeline + portable job adapter |
| `pocketbase/schema.json` | Coordination collections |

## Roadmap — verifiable milestones

1. **Local prototype** — HTML client, Fossil course, Markdown, quiz engine, local progress/XP, offline.
2. **AI factory** — BYOK, syllabus/lesson/Marp/quiz generation, schema validation, draft→review→publish.
3. **Pipelight assessment** — pipelines, Rust orchestration, restricted WASM, deterministic fixtures, signed reports.
4. **Peer collaboration** — repo sharing, discovery/sync, signed discussions, projects, local search.
5. **Portable credentials** — Ed25519 identities, credit policies, issuance/verification, revocation.
6. **Distributed governance** — replicated policy, cross-community recognition, ledger evaluation (only if justified).

## License

MIT per [LICENSE](LICENSE).
