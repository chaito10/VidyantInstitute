---
marp: true
theme: default
paginate: true
title: Vidyarthi — Peer-to-Peer, AI-Driven Micro-Learning University (v0.1)
---

## Vidyarthi — Digital Distributed University

- Peer-to-peer, AI-assisted micro-learning university (White Paper v0.1, Oct 2026)
- **Local-first**: study offline, sync with peers when available
- Versioned courses · minimal client · automated assessment · BYOK AI · signed credentials
- **No blockchain required** for the initial release

---

## Design principles (§1.3)

- Local-first · repository-native · AI-assisted, human-accountable
- Provider-independent · composable · open and inspectable
- Evidence-based · portable · resource-efficient · security by design

---

## Six logical layers (§2)

| Layer | Technology |
|---|---|
| Learning interface | HTML5, vanilla JS, CSS |
| Academic content | Fossil SCM, Markdown, JSON |
| Coordination | PocketBase |
| AI assistance | BYOK adapters, local endpoints |
| Execution & assessment | Pipelight, Rust, WASM |
| Distribution & trust | Fossil sync, optional libp2p, pubkey crypto |

---

## Courses as versioned artifacts (§3)

- Each course: a Fossil repository (syllabus, lessons, quizzes, rubrics, media)
- `course.json` manifest: id, version, outcomes, modules, license, hashes
- Credits are **descriptive metadata** — never auto-entitlements
- Release = pinned revision; learners assess against that revision

---

## AI + BYOK (§4)

- No central provider: hosted, OpenAI-compatible, Ollama / llama.cpp, institutional gateways
- Keys in memory by default; never in repos, peers, assets, or logs
- Pipeline: plan → lessons → Marp slides → assessments → media → validation → human review
- Tutor: course-grounded, cites sources, hints before solutions

---

## Assessment with Pipelight (§5)

- Portable job schema → adapter → pipeline steps
- Restricted runner (WASM/Rust): no network, capped time/memory
- Report: hashes, revisions, outcomes, score + rationale, signer, timestamp
- Execution proves tests passed — **authorization stays human**

---

## P2P, gamification, credentials (§6–§8)

- Offline queues; per-type conflict rules — **never last-write-wins** for academic records
- XP rewards activity; **competency requires evidence**; credits need policy
- Ed25519 signed credentials; community vs institution vs legally-recognized
- Revocation is append-only; **no token, no cryptocurrency**

---

## Deployment & roadmap (§9–§12)

- Profile A personal → B community (+PocketBase/P2P) → C institutional (+issuers)
- Phase I local prototype → II AI factory → III Pipelight → IV P2P → V credentials → VI governance
- MVP: one Fossil course, one HTML client, quiz engine, BYOK, validation, signed results

---

## Thank You

- Spec: `white_paper.md` (from `Vidyarthi_White_Paper.docx`)
- Prototype: `public/vidyarthi.html` · sample: `courses/cybersecurity-101/`
- Open, inspectable, and portable by design
