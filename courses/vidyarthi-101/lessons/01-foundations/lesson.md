# Lesson 1 — Foundations: vision, principles, layers

Outcome: `foundations` (syllabus outcome 1). Spec: §1–§2.

## What Vidyarthi is

Vidyarthi is a **peer-to-peer, AI-driven micro-learning university**: learning
resources, practical assessment, peer collaboration, and portable academic
achievements delivered through a lightweight, **offline-capable** environment.

## Local-first, not unconditionally decentralized

Learners study and complete supported activities **without continuous
connectivity**. Peer networks provide replication, collaboration, and
synchronization **when available**. A small deployment can be just a browser, a
local Fossil repository, a local assessment process, and PocketBase.

## Design principles (§1.3)

- **Local-first**: core learning works offline.
- **Repository-native**: courses are versioned artifacts, not database rows.
- **AI-assisted, human-accountable**: AI never confers academic authority.
- **Provider-independent**: learners choose AI providers, including local models.
- **Composable / open / evidence-based / portable / resource-efficient.**
- **Security by design**: validate untrusted content at trust boundaries (§10).

## Six logical layers (§2)

| Layer | Technology |
|---|---|
| Learning interface | HTML5, vanilla JS, CSS |
| Academic content | Fossil SCM, Markdown, JSON |
| Application coordination | PocketBase (NOT canonical authority) |
| AI assistance | BYOK adapters, local endpoints |
| Execution & assessment | Pipelight, Rust, WASM |
| Distribution & trust | Fossil sync, optional libp2p, pubkey crypto |

Layers are **logical, not mandatory servers**.
