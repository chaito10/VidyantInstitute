# Vidyarthi — Decision Log & Open Questions

**Updated:** 22 October 2026  
**Status:** Working project decisions derived from the user's latest answers.

## 1. Product identity and scope

- **Canonical product name:** Vidyarthi.
- **Long-term vision:** An open learning ecosystem spanning Foundation through PhD-level work.
- **First product:** An AI-generated MOOC composed of consistently structured micro-learning modules.
- **MVP target:** A complete course usable on a phone or laptop.
- **Course format:** Consistent micro-learning format across modules. Individual peers can publish without mandatory authorization or peer verification.
- **AI:** Bring-your-own-key (BYOK) integrations. Default is automated assessment; human involvement triggered by grievance.

## 2. Participants and review

- **Participant model:** Flat participants, no permanent platform-wide authority or rank.
- **Peer review:** Optional, open, opt-in for papers/theses. Not a publishing prerequisite.
- **Governance:** No governance model. Implications for credential claims, grievance resolution, and software maintenance remain unresolved.
- **Authority boundary:** "No authority" is the stated direction. How government/industry validation, wallet uniqueness, credential issuance, and grievance resolution occur without an authority model is unresolved.

## 3. Assessment, evidence, and credentials

- **Assessment:** Automated assessment is the default for all assessments.
- **Human intervention:** No routine human involvement unless a grievance is raised. The grievance/appeal path is unresolved.
- **Evidence:** "Blockchain, human lifetime" — preference for blockchain-backed evidence with lifetime retention (interpretation not yet confirmed).
- **Credentials:** Prioritize real projects, assignments, and government/industry validation as evidence for employer competency claims.
- **Credits:** Generate descriptive credits and quantitative measures; compilable into program results.
- **Verification:** Credits on an open blockchain, verifiable by anyone.
- **PhD-equivalence:** If work is equivalent to a PhD, it is a PhD. This is a competency-equivalence principle, not a claim that the platform can legally award degrees.

## 4. Identity, privacy, and technology

- **Identity:** A wallet, intended to be unique per person.
- **Security:** Web3 security standards; specific standards and threat model not yet selected.
- **Data privacy:** Records local; ZK apps for verification. Needs reconciliation with open-blockchain/public-verification.
- **Peer distribution:** Fossil SCM plus libp2p preferred.
- **Technology interests:** Web3, wallets, ZK apps, Fossil, Rust.
- **Blockchain cost:** Zero overhead; costs borne by student if overhead cannot be avoided.
- **Warranty/liability:** No warranty or liability. Legal review required.

## 5. What these decisions do not establish

- No employer recognition, government validation, accreditation, or legal recognition.
- No claim that platform-issued credentials equal formal academic degrees.
- No resolution of how blockchain verification coexists with local-only records and privacy.
- No resolution of grievance handling, fraud response, wallet uniqueness, key recovery, or protocol changes.

## 6. Implementation order

1. Build minimal AI-generated micro-course; prove complete module on phone/laptop.
2. Define versioned course/module format, BYOK adapter interface, automated assessment/evidence format.
3. Define flat-participant and grievance model before implementing authority-sensitive behavior.
4. Prototype wallet-based identity and local/ZK verification; benchmark public-chain costs and privacy before committing personal data.
5. Validate employer-facing evidence with real projects and assignments.
6. Keep formal degree claims separate from competency equivalence until a recognized awarding pathway is established.

## Unresolved questions

| # | Topic | Key question |
|---|-------|-------------|
| Q1 | Flat participation | Does "no authority" rule out temporary issuer/assessor/grievance roles? |
| Q2 | MVP scope | Subject, learner level, mandatory micro-module fields, quality gates |
| Q3 | Employer credentials | Which government/industry partners? What counts as validation? |
| Q5 | Credits definition | Learning-effort units, competency measures, or formal academic credits? |
| Q7 | Compiled results | Quantitative measures, units, weighting, reproducibility |
| Q8 | Assessment integrity | Preventing fabricated tests, handling false positives and appeals |
| Q9 | Grievances | Who receives/decides grievances without governance? |
| Q10 | Evidence retention | On-chain vs local? Personal data on immutable ledger? |
| Q13 | Local vs blockchain | Raw records local; selective proof publication? |
| Q15 | Governance | No voting/DAO/central admin? Minimal process for incidents? |
| Q19 | Standards | Specific interoperable standards for modules, assessment, evidence, wallet, credentials |
| Q21 | Blockchain overhead | Zero platform fee? Which chain? In MVP or later? |
| Q23 | Protocol | Module contract, reference runner, deterministic I/O, versioning |
