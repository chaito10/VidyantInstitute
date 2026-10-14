# Vidyarthi — Digital Distributed University

> **Repo renamed:** `charudatta10/SageEduMint` → `charudatta10/VidyantInstitute`.
> Local origin updated to `https://github.com/charudatta10/VidyantInstitute.git`.
> Product spec renamed: **SageEduMint / OpenDAO University → Vidyarthi** per
> `Vidyarthi_White_Paper.docx` (v0.1 — Initial Proposal, 11 Oct 2026, status: Proposed architecture).

Vidyarthi is a **peer-to-peer, AI-driven micro-learning university**: version-controlled
course repositories, a minimal offline-capable web client, automated assessment pipelines,
user-controlled AI providers, peer networking, gamification, and cryptographically
verifiable credentials. **Local-first, not unconditionally decentralized.**

Full spec: [white_paper.md](white_paper.md) (distilled from `Vidyarthi_White_Paper.docx`).
Courses: [`courses/cybersecurity-101/`](courses/cybersecurity-101/) (sample) and
[`courses/vidyarthi-101/`](courses/vidyarthi-101/) (**Vidyarthi Platform Orientation** —
this repo's documentation as a micro-course: 4 lessons with Marp slides, quizzes,
exercises, rubric, and capstone project).
Single-file client prototype: [`public/vidyarthi.html`](public/vidyarthi.html).

## What changed (SageEduMint/OpenDAO → Vidyarthi v0.1)

| Before | Now (v0.1) |
| --- | --- |
| DAO governance + tokenized voting, NFT degrees | Explicit academic roles, **no token/cryptocurrency**; signed portable credentials (§8) |
| Blockchain-first (Celestia + EVM rollup, ERC-721) | **Blockchain deferred** — signed records + append-only history first (§8.4) |
| IPFS/OrbitDB/Ceramic, Filecoin, Kademlia DHT + torrents | **Fossil SCM** for courses + sync; **PocketBase** coordination only; optional Rust/libp2p peer service |
| Next.js/React, Tailwind/Alpine PWA | **Single HTML5 + vanilla JS/CSS** client, WASM for portable execution (§9.1) |
| Ollama-only AI | **BYOK**: hosted, OpenAI-compatible, Ollama/llama.cpp, institutional gateway; keys memory-only (§4) |
| Ad-hoc grading scripts | **Pipelight CI** pipelines + restricted Rust/WASM runner, versioned rubrics, signed reports (§5) |
| XP/reputation mixed with credentials | **XP ≠ competency**: engagement, reputation, competency, credits tracked separately (§7) |

Legacy OpenDAO/SageEduMint code (Next.js app, Express server, PoW chain, NFT minting,
DHT/torrent sharing, DAO voting, wallet identity, PUCL tiers) was **removed in v0.2.0**
(see [CHANGELOG.md](CHANGELOG.md)). Implementation lives in [`src/vidyarthi/`](src/vidyarthi/)
with schemas in [`schemas/`](schemas/); [`src/security/`](src/security/) holds the §10
access-control/privacy helpers.

## Architecture — six logical layers (§2)

| Layer | Responsibility | Proposed technology |
| --- | --- | --- |
| Learning interface | Lessons, quizzes, dashboards, offline interaction | HTML5, vanilla JS, CSS |
| Academic content | Course packages, history, projects, references | Fossil SCM, Markdown, JSON |
| Application coordination | Accounts, discovery, sync metadata (NOT canonical authority) | PocketBase |
| AI assistance | Tutoring, generation, feedback | BYOK adapters + local endpoints |
| Execution & assessment | Validation, test execution, scoring | Pipelight, Rust, WASM |
| Distribution & trust | Peer sync, signed results, credentials | Fossil sync, optional libp2p, Ed25519 |

Deployment profiles: **A** personal (browser + local repos + optional local AI) →
**B** community (+ PocketBase, P2P sync, assessment jobs) → **C** institutional
(+ authorized assessors, issuer keys, governance). All share course/credential formats.

## Getting started

Requirements: **Python ≥ 3.13** (no Node.js dependencies — the client is dependency-free
vanilla HTML/JS/CSS). Clone:

```bash
git clone https://github.com/charudatta10/VidyantInstitute.git
cd VidyantInstitute
```

## Quickstart (Phase I — local learning loop)

```bash
# 1. Validate the sample course (§3)
python scripts/validate_course.py courses/cybersecurity-101
# or: python main.py validate

# 2. Open the offline client (§9.1) — no build step; open in a browser:
# public/vidyarthi.html  (load course.json + quiz.json from the sample course)
# or serve it: npm run serve  (python http.server on :8080)

# 3. Run a portable assessment job (§5) — adapter translates to Pipelight steps
python scripts/run_assessment.py --job courses/cybersecurity-101/assessments/tests/basic.json

# 4. Run tests
python -m pytest tests/ -q
```

## Project structure

| Path | Contents (§ reference) |
| --- | --- |
| `white_paper.md` | Spec distilled from `Vidyarthi_White_Paper.docx` v0.1 |
| `docs/whitepaper-presentation.md` | Marp slide deck (§4.3 Stage 3 artifact example) |
| `src/vidyarthi/` | `course`, `assessment`, `credentials`, `byok`, `gamification`, `governance` (§11.1), `sync` (§6.2) |
| `src/security/` | Access control + data privacy helpers (§10) |
| `schemas/` | Course, assessment-job, assessment-result, credential JSON schemas |
| `courses/cybersecurity-101/` | Sample Fossil-ready course package (§3.2) |
| `courses/vidyarthi-101/` | Platform documentation as a micro-course (4 lessons + capstone) |
| `public/vidyarthi.html` | Single-file offline learning client (§9.1) |
| `pipelight/` + `scripts/` | CI pipeline + portable job adapter (§5) |
| `pocketbase/schema.json` | Coordination collections — not canonical authority (§9.2) |

## Roadmap (§12, Phase I–VI)

1. **Local learning prototype** — single-file client, Fossil course, Markdown+Marp, JSON quizzes, local XP. Exit: study + quiz offline.
2. **AI course factory** — BYOK config, syllabus/lesson/slide/quiz generation, schema validation, draft→review→publish.
3. **Pipelight assessment** — pipelines, Rust orchestration, restricted WASM, deterministic fixtures, signed reports.
4. **Peer collaboration** — repo sharing, discovery/sync, signed discussions, search, moderation.
5. **Portable credentials** — Ed25519 identities, credit policies, issuance/verification, revocation, export tests.
6. **Distributed governance** — replicated policy records, cross-community recognition, ledger evaluation (only if justified).

P2P networking, multimedia generation, consensus, and formal degrees do **not** block the MVP
(Appendix B): one Fossil course, one HTML client, quiz engine, XP/competency, BYOK,
Pipelight validation, restricted runner, signed result format, credential verifier.

## Contributing / License

See [CONTRIBUTING.md](CONTRIBUTING.md); MIT per [LICENSE](LICENSE).
