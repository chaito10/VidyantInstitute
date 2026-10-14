# Changelog

## [v0.2.0] - 2026-10-14

### Changed (Vidyarthi v0.1 realignment)
- Repo renamed `SageEduMint` → `VidyantInstitute`; product renamed to **Vidyarthi**
  per `Vidyarthi_White_Paper.docx` (v0.1, 11 Oct 2026).
- `white_paper.md` rewritten as a faithful distillation of the new whitepaper.
- New `src/vidyarthi/` core: course validation (§3), assessment jobs/reports (§5),
  signed credentials + append-only log (§8), BYOK adapters (§4), gamification (§7),
  governance roles (§11.1), sync conflict rules (§6.2).
- Added `schemas/`, sample `courses/cybersecurity-101/`, single-file
  `public/vidyarthi.html` client (§9.1), `pipelight/` pipeline, `scripts/`,
  `pocketbase/schema.json` (§9.2), Vidyarthi Marp deck.

### Removed (old OpenDAO/SageEduMint specification)
- Next.js pages + Express server + Tailwind PWA (`pages/`, `styles/`, `server.js`, `index.html`).
- Blockchain-first stack: PoW chain, ERC-721 NFT minting, DHT/torrent sharing
  (`src/blockchain.py`, `src/credentialing/`, `src/credential_mananger_service.py`,
  `sageedumint_prod.py`, DAO governance, wallet identity, PUCL tiers, Ollama-only prompts,
  dummy grading, Hugo/Zola SSG, legacy frontend).
- Stale locks and branding (`package-lock.json`, `uv.lock`, `assets/cover.png`,
  `gemini.md`, `prompt.md`, empty scaffolding files).
- Blockchain is **deferred** per §8.4; NFT/token mechanics are out of scope.

## [v0.1.0] - 2026-08-14

### Added
- Initial repository setup
- DHT-based credential manager service (`src/credential_mananger_service.py`)
- Runtime dependencies for bcrypt, bencodepy, kademlia, libtorrent, pyjwt, transmission-rpc, and transmissionclient
