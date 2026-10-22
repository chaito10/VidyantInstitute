# Vidyarthi — Open Questions and Decision Log

**Updated:** 22 October 2026  
**Purpose:** Record the user's current decisions and keep unresolved contradictions visible. The answers below are not silently converted into technical or legal guarantees.

## Confirmed current direction

- [x] Canonical product name: **Vidyarthi**.
- [x] Long-term scope: Foundation through PhD-level learning.
- [x] First product: AI-generated MOOC made of consistently formatted micro-learning content.
- [x] MVP: a complete course/module usable on a phone or laptop.
- [x] Course publishing: individual peers can design/publish content without mandatory authorization or peer review.
- [x] Peer review: optional, open, and opt-in for papers, theses, and other work.
- [x] Assessment: automated by default; human involvement only after a grievance.
- [x] Identity direction: wallet intended to be unique per person.
- [x] Preferred peer distribution: Fossil SCM + libp2p.
- [x] Technology interests: Web3, wallets, ZK apps, Fossil, Rust, and BYOK AI.
- [x] Credentials/evidence priority: real projects, assignments, and eventual government/industry validation.
- [x] Program pathways: multiple entry/exit points; accumulated credits may be compiled into programs.
- [x] Employer discovery: a portal for employers to search/query competency evidence.
- [x] Protocol direction: minimal, abstract, modular, and usable by others to run a complete module.

## Q1. Flat participation and “no authority”

**Decision given:** “Go with Flat participants no authority at all.”

**Still unresolved**
- Does “no authority” mean no permanent rank, or does it also rule out any temporary issuer, assessor, moderator, or grievance-resolution capability?
- If no participant can authorize or validate anything, how are government/industry attestations and wallet uniqueness represented?
- Who can respond to fraud, malicious course packages, abuse, or a grievance without creating a governance or authority mechanism?

**Do not implement:** Do not replace static roles with an invented capability-granting policy. The current target rejects permanent hierarchy, but the exact authorization model is unresolved.

## Q2. First MVP and course format

**Decision given:** Start with the first AI-generated MOOC, built from micro-learning content with a consistent format throughout; course requirements/design are peer-designed.

**Still unresolved**
- What subject and learner level should the first MOOC target?
- What exact fields are mandatory in every micro-learning module?
- Which AI-generated artifacts are accepted automatically, and what automated quality gates must pass before publication?
- What is the end-to-end MVP acceptance test on phone and laptop?

## Q3. Employer-facing credentials

**Decision given:** Use real projects, assignments, and validation from government and industries.

**Still unresolved**
- Which government bodies or industry partners, if any, are actual participants? None are assumed to be committed.
- What counts as validation: endorsement, an assessment rubric, a signed attestation, or hiring outcomes?
- How will the system distinguish community-issued, employer-endorsed, government-validated, accredited, and legally recognized credentials?

## Q4. Naming

**Decision given:** Name the product **Vidyarthi**.

**Decision updated:** Vidyarthi is now the canonical working product name. `VidyantInstitute` remains the repository name for now; `SageEduMint` and `OpenDAO University` are historical/working names.

**Still unresolved:** Should the repository name eventually be changed? This is not a blocker for the MVP.

## Q5. Pathways and credits

**Decision given:** Credits should be on an open blockchain and verifiable by anyone; learners have multiple entry/exit points independent of prior certification; accumulated credits may be formalized into programs.

**Still unresolved**
- Which blockchain or credential/record format is intended?
- Are “credits” learning-effort units, competency measures, or formal academic credits? These are not interchangeable.
- Who defines program thresholds and equivalencies if the platform has no governance or authorization model?
- How can open verification avoid publishing personal or sensitive learning records?

## Q6. Curriculum governance and peer review

**Decision given:** Individuals may publish without required authorization or verification. Peer review of papers/theses is optional and may use open comments; AI evaluation is sufficient as the default.

**Still unresolved**
- What automated validation is mandatory for course packages, assessments, generated references, and executable content?
- Can an author opt out of peer review while still making a credential claim based on the work?
- How are corrections, plagiarism allegations, and unsafe or malicious material handled without a governance mechanism?

## Q7. Credits and compiled results

**Decision given:** Generate descriptive and quantitative measures that can be compiled through a program into a final result for job scrutiny or other purposes.

**Still unresolved**
- Define each quantitative measure, its units, weighting, and reproducibility.
- Who chooses program compilation rules, and can employers interpret them consistently?
- How are changed rubrics or reassessed work reflected in historical results?

## Q8. Assessment

**Decision given:** All assessment should be automated.

**Still unresolved**
- Which assessment types can be reliably automated, and what happens when the model cannot grade confidently?
- What prevents generated tests from being fabricated, self-serving, or easy to game?
- How are false positives, accessibility needs, and appeals handled?

## Q9. Human intervention and grievances

**Decision given:** No human intervention is required until a grievance is raised.

**Still unresolved**
- Who receives and decides grievances if the system has no governance or authority model?
- What evidence, response times, appeal stages, and temporary safeguards apply?
- Can a disputed result be marked as contested without silently deleting the original evidence?

## Q10. Evidence and retention

**Decision given:** “It's blockchain, human life time.”

**Interpretation not yet confirmed:** This may mean blockchain-backed evidence retained for the person's lifetime.

**Still unresolved**
- Which data is on-chain, and which stays local or encrypted/off-chain?
- Does “lifetime” mean the learner's lifetime, the credential's lifetime, or permanent retention?
- How do key loss, correction, revocation, privacy, and deletion requests work with immutable records?

## Q11. Wallet identity

**Decision given:** A wallet, one unique wallet per person.

**Still unresolved**
- How is one-person-one-wallet established without collecting excessive identity data or introducing a central authority?
- Are pseudonymous wallets permitted? How are wallet recovery, key rotation, compromise, and succession handled?
- What evidence, if any, links a wallet to a legal person for employer/government validation?

## Q12. Web3 security

**Decision given:** Use Web3 standards for security.

**Still unresolved**
- Select the concrete wallet, signature, key-management, credential, and ZK proof standards.
- Define a threat model covering replay, malicious modules, key theft, Sybil identities, privacy leakage, and compromised dependencies.
- Which operations must be local-verifiable, and what happens when revocation information is unavailable offline?

## Q13. Local records and ZK verification

**Decision given:** All records are local; verification uses ZK apps.

**Blocking tension:** Q5 calls for open-blockchain credits verifiable by anyone, while Q10 suggests lifetime blockchain evidence. These can conflict with local-only records and privacy.

**Still unresolved**
- Does “all records local” mean raw personal records remain local while users selectively publish proofs/commitments?
- Which facts should a ZK proof reveal, and which must remain private?
- How are public verification, revocation, correction, and data minimization handled?

## Q14. Peer network

**Decision given:** Fossil SCM + libp2p is preferred.

**Still unresolved**
- Which data is synchronized through Fossil and which messages/services use libp2p?
- What are the MVP offline and sync-conflict acceptance tests?
- How are peers discovered and spam/malicious peers handled without a central authority?

## Q15. Governance

**Decision given:** “No governance model.”

**Blocking tension:** The project also expects grievances, employer/government validation, open credentials, automated assessment, and correction/revocation of evidence. These require defined procedures even if the project rejects platform-wide governance.

**Still unresolved**
- Does “no governance” mean no voting/DAO, no central administrators, or no shared policy at all?
- Can protocol maintainers publish software updates without controlling learner records or credentials?
- What minimal process, if any, exists for security incidents, grievances, and incompatible protocol versions?

## Q16. MVP acceptance criteria

**Decision given:** The complete course should work on a phone or laptop.

**Still unresolved**
- Which phone/browser and laptop/browser combinations are supported first?
- Must the course work fully offline after initial download?
- What is the minimum complete module: content, quiz, practical assignment, automated result, local evidence, and export?
- What resource limits and automated test suite define “works”?

## Q17. Warranty and liability

**Decision given:** No warranty or liability.

**Still unresolved**
- Draft appropriate terms and disclaimers with qualified legal review for the jurisdictions where the product is offered.
- Which legal obligations or liabilities cannot be excluded by contract?
- How are third-party AI providers, user-generated content, security issues, and credential misrepresentation addressed?

**Caution:** A “no warranty/liability” statement does not itself guarantee that all liability can legally be excluded.

## Q18. Costs and sustainability

**Decision given:** Costs are borne by peers or students.

**Still unresolved**
- Which costs are paid by students: AI inference, storage, blockchain fees, network bandwidth, hosting, or all of them?
- Must learning, local verification, and basic course access remain possible at zero monetary cost?
- Can BYOK/local AI avoid mandatory provider spending, and how are costs disclosed before a task runs?

## Q19. Standards and stack

**Decision given:** Web3, wallets, ZK apps, Fossil, and Rust.

**Still unresolved**
- Select specific interoperable standards rather than treating these technology categories as standards themselves.
- Define stable module, assessment, evidence, wallet, and credential interfaces.
- Which components are required for the first release, and which remain optional adapters?

## Q20. Employer search portal

**Decision given:** Build a portal that lets employers submit search queries.

**Still unresolved**
- What can employers search: public portfolio data, learner-approved evidence, credentials, or private records?
- Does a learner approve disclosure for each query or profile?
- How are ranking bias, stale evidence, and misleading credential labels avoided?

## Q21. Blockchain overhead

**Decision given:** Zero overhead; if costs are borne, they should be borne by the student.

**Still unresolved**
- Does “zero overhead” mean zero platform fee, zero gas fee, zero extra infrastructure, or negligible user effort?
- Which chain or layer is intended, and how will fees be measured on ordinary phones?
- Should blockchain be in the MVP, or should the MVP prove the learning loop before adding it?

## Q22. PhD-equivalent work

**Decision given:** “If work is equivalent to PhD it is a PhD.”

**Important distinction:** The platform can assess or document PhD-level work/competency, but that alone does not make it a formally awarded or legally recognized PhD degree. A formal degree claim depends on applicable law and a recognized awarding authority.

**Still unresolved**
- Should the platform issue a “PhD-level competency/research portfolio” record, while formal-degree status is shown separately?
- What standards and independent evaluation determine equivalence?
- Which recognized institution or legally authorized body, if any, can confer the formal degree?

## Q23. Protocol and tooling

**Decision given:** The protocol and tools should let anyone run a complete module; keep the design minimal, abstract, modular, and BYOK for AI.

**Still unresolved**
- Define the module contract and the smallest reference runner.
- Specify deterministic inputs/outputs, assessment interfaces, evidence export, and compatibility/versioning.
- Define what “anyone can run” means for offline use, supported hardware, dependencies, and AI provider configuration.

## Cross-document update checklist

- [ ] README: canonical name Vidyarthi; first AI-generated micro-course; MVP on phone/laptop; no unsupported accreditation claims.
- [ ] White paper: reflect flat participation, optional peer review, automated assessment with grievance path, wallet/ZK privacy, and the open blockchain/local-record tension.
- [ ] `src/vidyarthi/governance.py`: do not rewrite until “no authority” versus issuer/appeal needs is resolved.
- [ ] Credential/evidence code: keep competency evidence distinct from employer endorsement, government validation, accreditation, and formal degrees.
- [ ] Schemas: define module, assessment, quantitative/descriptive credit, wallet, proof, and evidence formats.
- [ ] Tests: complete module on phone/laptop; offline behavior; automated grading; grievance state; privacy-preserving verification.
- [ ] Legal/terms review before making “no liability,” government validation, or PhD claims.

## Decision log

| Date | Topic | Current decision | Status |
|---|---|---|---|
| 2026-10-22 | Name | Vidyarthi | Confirmed |
| 2026-10-22 | MVP | AI-generated MOOC, consistent micro-learning modules, phone/laptop | Confirmed direction; acceptance criteria open |
| 2026-10-22 | Participants | Flat participants; no authority intended | Ambiguous against validation and grievance requirements |
| 2026-10-22 | Assessment | Automated by default; human involvement after grievance | Direction confirmed; appeal mechanism open |
| 2026-10-22 | Credits | Descriptive and quantitative; compile into program results | Direction confirmed; definitions open |
| 2026-10-22 | Verification | Open blockchain + local records + ZK apps | Architecture conflict unresolved |
| 2026-10-22 | Peer network | Fossil SCM + libp2p | Preferred |
| 2026-10-22 | Formal qualifications | PhD-level work should be recognized as equivalent | Formal degree versus competency status unresolved |
