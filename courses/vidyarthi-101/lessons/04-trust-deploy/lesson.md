# Lesson 4 — Sync, gamification, credentials, deployment

Outcome: `trust-deploy` (syllabus outcome 5). Spec: §6–§9.

## Peer sync (§6)

Exchange repos, discussions, artifacts, reviews, signed records. Study offline,
queue changes, sync on reconnect. Conflicts are **per-type**: history-merge for
content, identity+ordering for discussions, explicit event rules for progress —
and **credentials are verified as signed records, never merged**. No
last-write-wins for academic records (see `src/vidyarthi/sync.py`).

## Gamification (§7) — XP ≠ competency

| Mechanism | Purpose | NOT |
|---|---|---|
| XP / streaks | activity, regularity | competence, quality |
| Levels / badges | milestones | qualifications |
| Reputation | useful contributors | formal expertise |
| Competency records | demonstrated outcomes | auto-degree eligibility |
| Credits | policy-bound achievement | universal recognition |

Anti-gaming: rate limits, randomized variants, independent reviewers, evidence,
anomaly detection, reassessment.

## Credentials without blockchain (§8)

Ed25519 signed records + append-only history first; consensus only if governance
demands it. Lifecycle: eligibility → verify → authorize → **sign** → distribute
→ verify → revoke-by-new-record (never overwrite). UIs must separate
**community / institution / legally-recognized** credentials. **No tokens.**

## Deploy (§9)

Single-file HTML5 client (WASM/assets split if large). PocketBase coordinates
accounts/discovery/sync/notifications/caches — never canonical. Profiles:
**A** personal → **B** community → **C** institutional.
