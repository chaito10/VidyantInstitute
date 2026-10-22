# Vidyarthi — Unanswered Questions and Decision Log

> **Purpose:** Working checklist for questions that remain unresolved in the Vidyarthi university project. Fill in the **Your decision** fields when ready. Do not treat proposals or earlier working names as canonical unless explicitly approved.
>
> **Context:** The repository currently uses the names Vidyarthi and VidyantInstitute, with SageEduMint and OpenDAO University retained as working names/aliases while the final canonical name is deferred. This checklist reflects the latest confirmed direction shared in project discussions as of 22 October 2026.

## How to use this file

- Replace `[Your answer here]` with a decision, or write `Defer` with a reason.
- Keep disputed or contradictory decisions visible until resolved.
- Once a decision is approved, update the relevant specification, implementation, tests, and changelog in the same change.
- Do not treat a credential as employer-recognized, institutionally accredited, or legally recognized unless the relevant recognition has actually been established.

## 1. Confirmed direction — do not reopen without reason

These are current decisions, not unanswered questions:

- [x] **Naming:** Decide the final canonical name later; retain existing names as working titles/aliases for now.
- [x] **Scope:** Long-term vision spans Foundation through PhD; begin with a small, verifiable MVP.
- [x] **Credentials:** Prioritize employer-recognized skills and competency credentials.
- [x] **Participant model:** Flat participant model, with temporary, capability-based permissions rather than permanent rank-based roles.

## 2. Blocking design contradictions

### Q1. Flat participants versus role-based authorization

**Why this is open:** The current `white_paper.md`, `src/vidyarthi/governance.py`, README, and credential logic describe explicit roles such as course reviewer, assessment operator, and credential issuer. The latest direction is a flat participant model with temporary, capability-based permissions.

**Questions**
- What grants a capability: self-declaration, peer delegation, evidence, community policy, or issuer authorization?
- Who may grant, scope, expire, suspend, or revoke a capability?
- Should high-impact capabilities require multiple independent approvals?
- How are issuer authority and legal/institutional recognition represented without permanent user ranks?

**Your decision:** [Your answer here]

### Q2. Scope of the first MVP

**Why this is open:** The long-term vision spans Foundation through PhD, but the repository's MVP is a local learning loop with course packages, quizzes, AI assistance, assessment, and credential verification.

- Which single learning journey must work end-to-end in the MVP?
- Which learner level or subject will be used for the first demonstrator?
- Which proposed components are mandatory at MVP launch, and which remain prototypes or future phases?

**Your decision:** [Your answer here]

### Q3. Meaning of employer-recognized credentials

- What evidence makes a skill or competency credential credible to employers?
- Will employer recognition start through a small advisory/pilot group, hiring partners, practical challenge results, independent assessors, or another route?
- Should credentials contain evidence links, reproducible test results, project artefacts, rubric versions, assessor attestations, and confidence/limitations?
- How should the platform label community-issued credentials versus employer-endorsed, institution-issued, accredited, or legally recognized qualifications?

**Your decision:** [Your answer here]

### Q4. Name and brand transition

- Which names remain historical aliases, and which should appear in the UI or documentation during the transition?
- Should the repository name `VidyantInstitute` remain even if the eventual product name changes?
- What event or milestone triggers a canonical-name decision?

**Your decision:** [Your answer here]

## 3. Academic model and learning pathways

### Q5. Foundation-to-PhD pathway structure

- How should the platform represent the stages Foundation, school-level learning, undergraduate, postgraduate, research, and PhD-level work?
- Are these formal programs, competency maps, optional pathways, or just discovery labels?
- Can participants enter at any level based on demonstrated competency rather than prior certificates?
- Who defines prerequisites, equivalencies, and progression rules?

**Your decision:** [Your answer here]

### Q6. Curriculum governance

- Who can propose, review, publish, fork, deprecate, and archive course revisions?
- Which decisions require independent peer review or subject-matter review?
- Is there a distinction between community curriculum approval and employer/institution endorsement?
- What appeal path exists when a course or assessment is rejected?

**Your decision:** [Your answer here]

### Q7. Credits and qualifications

The current specification says credits are descriptive unless an authorized policy assigns value.

- Should the MVP omit credit totals entirely, retain descriptive credits, or model workload/credit systems from the start?
- How are competencies composed into larger certificates or qualifications?
- Who owns equivalency mappings across communities and external frameworks?

**Your decision:** [Your answer here]

## 4. Assessment, AI, and evidence

### Q8. Assessment modes and human oversight

- Which assessments can be fully automated, and which require human review?
- What level of independent review is required for high-stakes outcomes?
- How will rubric changes, appeals, re-submissions, suspected cheating, and assessor conflicts be handled?
- Should a learner be allowed to challenge an AI-generated score before it becomes part of an issued credential?

**Your decision:** [Your answer here]

### Q9. Agentic AI responsibilities

- Which tasks may AI agents perform autonomously: drafting courses, generating tests, reviewing submissions, conducting oral assessments, recommending pathways, or proposing credentials?
- Which actions always require a human or authorized capability-holder?
- How will generated content, code, tests, and claims be traced to model/provider/version and reviewed?
- What limits apply to cost, rate, privacy, data retention, and local-model operation?

**Your decision:** [Your answer here]

### Q10. Evidence quality and reproducibility

- What is the minimum evidence bundle for a competency credential?
- How long must assessment artefacts and rubrics remain available?
- How will results be reproduced when the execution environment, model, or dependencies change?
- What quality gates prevent fabricated references, tests that merely pass themselves, or low-quality AI-generated course material?

**Your decision:** [Your answer here]

## 5. Identity, privacy, trust, and governance

### Q11. Identity model

- Is an account or persistent public key needed for ordinary learning?
- Can participants learn and submit work pseudonymously?
- What evidence binds a person or organization to an issuer key when that binding is required?
- What happens after key loss, compromise, rotation, or transfer of an organizational issuer?

**Your decision:** [Your answer here]

### Q12. Capability lifecycle and security

- What is the capability format and scope (action, resource, audience, expiry, delegation, limits)?
- Should capabilities be signed, locally verifiable, and revocable?
- How are replay, privilege escalation, collusion, Sybil activity, and conflicting capability grants prevented or detected?
- Which actions require short-lived capabilities or multi-party approval?

**Your decision:** [Your answer here]

### Q13. Data privacy and portability

- Which records are local-only by default, and which can sync to peers?
- What are the rules for deletion requests when copies or credential evidence have been replicated?
- How should confidential research, unpublished papers, minors' data, and sensitive submissions be handled?
- Which export format should learners use to back up and migrate their data?

**Your decision:** [Your answer here]

### Q14. Peer network versus optional central services

- Which functions must work fully offline?
- Which functions may use a hosted coordination service without becoming dependent on it?
- Is Fossil plus optional libp2p still the preferred approach, or should an alternative be benchmarked before implementation?
- What are the acceptance tests for recovery, conflict resolution, peer discovery, spam resistance, and network outages?

**Your decision:** [Your answer here]

### Q15. Governance model

- How are shared policies proposed and changed in a flat participant system?
- Is governance per course, per community, per issuer, or platform-wide?
- What stops wealth, popularity, or compute ownership from creating de facto permanent hierarchy?
- Is a replicated ledger ever needed, and what concrete failure of signed append-only records would justify one?

**Your decision:** [Your answer here]

## 6. MVP delivery and sustainability

### Q16. MVP acceptance criteria

- What is the one command or documented sequence that demonstrates a complete local learning and assessment cycle?
- Which tests must pass before calling the MVP usable?
- What are the target limits for startup time, storage, memory, offline support, and ordinary hardware?
- What security review is required before running untrusted submissions?

**Your decision:** [Your answer here]

### Q17. Deployment and operational ownership

- Which deployment profile (personal, community, institutional) is the first supported target?
- Who hosts any shared services, and what data do they retain?
- What backup, restore, update, and migration procedures are required?
- What is the minimum support/maintenance promise for course packages and credential verification?

**Your decision:** [Your answer here]

### Q18. Sustainability and access

- Which services must remain free to use and verify?
- Which costs can be covered by grants, donations, institutional hosting, employer partnerships, or optional paid services?
- What safeguards prevent paid services from becoming a gate to learning or credential verification?
- Who pays for hosted AI or compute when the learner does not bring their own provider?

**Your decision:** [Your answer here]

## 7. Standards, interoperability, and recognition

### Q19. External formats and standards

- Which existing standards should be evaluated for verifiable credentials, learning outcomes, skills, assessments, accessibility, and course metadata?
- Which integrations are required for the initial employer pilot?
- What export/import tests define practical interoperability?

**Your decision:** [Your answer here]

### Q20. Employer feedback loop

- How will employers search and evaluate portfolios or competency evidence without turning the platform into a popularity ranking?
- What feedback can employers provide, and can participants contest or hide it?
- Will there be a pilot with named employers or industry partners before claiming recognition?

**Your decision:** [Your answer here]

## 8. Questions to resolve after the MVP proves value

### Q21. Blockchain and consensus

- What actual multi-party coordination requirement cannot be met by signatures, versioned repositories, and append-only logs?
- What threat model and governance membership would a ledger need to satisfy?
- What evidence would justify the maintenance, privacy, and recovery costs of consensus?

**Your decision:** [Your answer here]

### Q22. Research and doctoral pathways

- How are research proposals, supervisors/mentors, research ethics, peer review, reproducibility, and thesis milestones represented?
- How can external experts participate without receiving permanent platform-wide authority?
- How do research achievements map to competency evidence while clearly distinguishing platform-issued credentials from formal PhD degrees?

**Your decision:** [Your answer here]

### Q23. Open-source project boundaries

- What belongs in this repository versus separate specifications, course repositories, deployment tooling, and reference implementations?
- Which root-level spec convention will be used (for example, design spec, architecture decision records, or technical note)?
- Which white papers are planned, and what claims/evidence/review process must each include?

**Your decision:** [Your answer here]

## 9. Cross-document consistency checklist

After answering questions, check all of the following for alignment:

- [ ] `README.md` — current direction, MVP scope, setup instructions, links.
- [ ] `white_paper.md` — vision, participant model, capability lifecycle, credential recognition caveats.
- [ ] `Vidyarthi_White_Paper.docx` — archival source reconciled with the approved spec.
- [ ] `src/vidyarthi/governance.py` — flat participant and scoped temporary capability design.
- [ ] `src/security/` — authorization, revocation, validation, and audit policy.
- [ ] `src/vidyarthi/credentials.py` — evidence, issuer authority, recognition labels, revocation.
- [ ] `schemas/` — versioned course, assessment, result, capability, and credential schemas.
- [ ] `public/vidyarthi.html` — learner-facing language does not imply unsupported recognition or completed features.
- [ ] `courses/vidyarthi-101/` — orientation material matches the approved platform model.
- [ ] Tests and CI — enforce the approved rules and reject contradictory states.
- [ ] `CHANGELOG.md` — record approved behavioral and architectural changes.

## Decision log

| Date | Question | Decision | Status |
|---|---|---|---|
| 2026-10-22 | Naming | Final canonical name deferred; current names remain working titles | Confirmed |
| 2026-10-22 | Scope | Foundation-to-PhD long-term vision; small MVP first | Confirmed |
| 2026-10-22 | Credentials | Prioritize employer-recognized skills and competency credentials | Confirmed |
| 2026-10-22 | Participants | Flat participants with temporary capability-based permissions | Confirmed |
