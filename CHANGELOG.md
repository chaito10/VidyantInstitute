# Changelog

## [v0.3.0] - 2026-10-22

### Changed (consolidation pass)
- Removed stale SageEduMint/OpenDAO references from README, docs, CONTRIBUTING, and CHANGELOG.
- Consolidated `docs/OPEN_QUESTIONS.md` + `docs/PROJECT_DECISIONS.md` → `docs/DECISIONS.md`.
- Removed empty `src/` subdirectories: `governance`, `content`, `credentialing`, `evaluation`, `licensing`, `registration`, `syllabus`.
- Removed dummy `src/security/access_control.py` and `src/security/data_privacy.py` (stub print-based code contradicts the scoped-role design in `src/vidyarthi/governance.py`).
- Archived `sageedum_data/` → `sageedum_data_archive/` (untracked SageEduMint runtime data).
- Removed `.gitattributes` (empty).
- Rewrote README, CONTRIBUTING, and CHANGELOG to reflect current Vidyarthi state.
- Synced `pyproject.toml` and `package.json` version to 0.3.0.

### Removed (old SageEduMint/OpenDAO specification)
- `sageedum_data/` (users.json, torrents, logs — SageEduMint runtime data, archived).
- Dummy security stubs (`src/security/`) — replaced by scoped-role logic in `src/vidyarthi/governance.py`.
- `tests/test_security.py` — tested the removed security stubs.

## [v0.2.0] - 2026-10-14

### Added
- `src/vidyarthi/` core: course validation (§3), assessment jobs/reports (§5),
  signed credentials + append-only log (§8), BYOK adapters (§4), gamification (§7),
  governance roles (§11.1), sync conflict rules (§6.2).
- `schemas/`, sample `courses/cybersecurity-101/`, single-file
  `public/vidyarthi.html` client (§9.1), `pipelight/` pipeline, `scripts/`,
  `pocketbase/schema.json` (§9.2), Vidyarthi Marp deck.

### Removed (old OpenDAO/SageEduMint specification)
- Next.js pages + Express server + Tailwind PWA.
- Blockchain-first stack: PoW chain, ERC-721 NFT minting, DHT/torrent sharing, DAO governance.
- Stale locks and branding (`package-lock.json`, `uv.lock`, `assets/cover.png`, `gemini.md`, `prompt.md`).

## [v0.1.0] - 2026-08-14

### Added
- Initial repository setup with DHT-based credential manager service.
