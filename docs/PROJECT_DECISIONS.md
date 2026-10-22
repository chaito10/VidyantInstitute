# Vidyarthi — Project Decisions

**Updated:** 22 October 2026  
**Status:** Working project decisions derived from the user's latest answers. This document records intent; it does not claim the implementation, external recognition, or legal status already exists.

## 1. Product identity and scope

- **Canonical product name:** Vidyarthi. `VidyantInstitute` remains the repository name for now; `SageEduMint` and `OpenDAO University` are historical/working names.
- **Long-term vision:** An open learning ecosystem spanning Foundation through PhD-level work.
- **First product:** An AI-generated MOOC composed of consistently structured micro-learning modules.
- **MVP target:** A complete course that can be used on a phone or laptop. Keep the protocol and tooling minimal, abstract, modular, and usable by others to run a complete module.
- **Course format:** Use a consistent micro-learning format across modules. Course requirements/design are peer-designed; individual peers can publish without mandatory authorization or peer verification.
- **AI:** Use bring-your-own-key (BYOK) AI integrations. The intended default is automated assessment and evaluation; human involvement is triggered when a grievance is raised.

## 2. Participants and review

- **Participant model:** Flat participants, with no permanent platform-wide authority or rank.
- **Peer review:** Optional, open, and opt-in for work such as papers and theses; it can take the form of public comments. It is not a prerequisite for publishing.
- **Governance:** The stated preference is no governance model. The implications for shared protocol changes, abuse handling, grievances, credential claims, and software maintenance remain unresolved.
- **Authority boundary:** “No authority” is recorded as the user's stated direction. The project still needs to define how government/industry validation, wallet uniqueness, credential issuance, grievance resolution, and formal qualification claims can occur without introducing an authority model.

## 3. Assessment, evidence, and credentials

- **Assessment:** Automated assessment is the default for all assessments.
- **Human intervention:** No routine human intervention unless a grievance is raised. The grievance and appeal path remains to be designed.
- **Evidence and retention:** The answer given was “blockchain, human life time.” Treat this as a preference for blockchain-backed evidence and lifetime retention, not a complete retention/privacy policy.
- **Credentials:** Prioritize real projects, assignments, and validation from government and industry as evidence for employer-facing competency claims.
- **Credits:** Generate descriptive credits and quantitative measures. These may be compiled across a program into a final result for job scrutiny or other evaluation.
- **Program pathways:** Support multiple entry and exit points independent of prior certification. Accumulated credits may be formalized into programs.
- **Verification:** The stated goal is that credits earned are recorded on an open blockchain and can be verified by anyone.
- **PhD-equivalence intent:** The user stated that if work is equivalent to a PhD, it is a PhD. This is recorded as a competency-equivalence principle, not as a claim that the platform can legally award or confer a recognized PhD degree without the relevant recognized awarding authority.

## 4. Identity, privacy, and technology

- **Identity:** A wallet, intended to be unique per person.
- **Security direction:** Use Web3 security standards; the specific standards and threat model are not yet selected.
- **Data privacy:** Keep records local; use ZK apps for verification. This needs reconciliation with the open-blockchain / public-verification decision, especially for personal data and immutable records.
- **Peer distribution:** Fossil SCM plus libp2p is the preferred approach.
- **Technology interests:** Web3, wallets, ZK apps, Fossil, and Rust.
- **Blockchain cost constraint:** The stated preference is zero overhead, with costs borne by the student if overhead cannot be avoided. The cost model and meaning of “zero overhead” need clarification.
- **Service costs:** “Peer or student” is the current answer for who bears costs. The split between learner-hosted compute, hosted AI, community services, and other infrastructure remains open.
- **Employer discovery:** Provide a portal through which employers can submit queries/search for relevant competency evidence. The search and privacy model remains open.
- **Warranty/liability:** The stated product preference is no warranty or liability. Legal terms, consumer protections, and non-excludable liability require qualified legal review; a disclaimer alone may not remove legal obligations.

## 5. What these decisions do not establish

- They do not establish employer recognition, government validation, accreditation, or legal recognition. Those require actual relationships, endorsements, or applicable authorization.
- They do not establish that a platform-issued competency credential is the same as a formal academic degree.
- They do not mean the current static-role authorization code has been migrated.
- They do not resolve how public blockchain verification can coexist with local-only personal records, privacy, deletion, and lifetime retention.
- They do not resolve grievance handling, fraud/abuse response, wallet uniqueness, key recovery, or protocol change management.

## 6. Implementation order

1. Build the minimal, consistently structured AI-generated micro-course and prove a complete module on phone and laptop.
2. Define a versioned course/module format, BYOK adapter interface, and automated assessment/evidence format.
3. Define the flat-participant and grievance model before implementing authority-sensitive behavior.
4. Prototype wallet-based identity and local/ZK verification; benchmark public-chain costs and privacy implications before committing personal data to an immutable ledger.
5. Validate employer-facing evidence with real projects and assignments; describe government/industry validation only after it exists.
6. Keep formal degree claims separate from competency equivalence until a recognized awarding pathway is established.
