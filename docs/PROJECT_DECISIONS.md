# Vidyarthi Project Decisions

**Status:** Working decisions, updated 22 October 2026. This document records current direction, not a finalized canonical brand or a claim that all architecture is already implemented.

## Confirmed decisions

1. **Naming remains open.** Do not appoint a canonical product name yet. Vidyarthi, VidyantInstitute, SageEduMint, and OpenDAO University remain working names/aliases while naming is evaluated. The GitHub repository remains `VidyantInstitute` for now.
2. **Long-term scope:** envision an education ecosystem spanning Foundation through PhD.
3. **Delivery strategy:** start with a small MVP and expand incrementally; avoid making P2P scale, consensus, full credentialing, or formal-degree pathways prerequisites for proving the first learning journey.
4. **Credential priority:** prioritize demonstrable, employer-relevant skills and competency evidence. Employer recognition is a goal, not an existing guarantee. Clearly distinguish community-issued, employer-endorsed, institution-issued, accredited, and legally recognized awards.
5. **Participant model:** use a flat participant model with temporary, scoped, capability-based permissions rather than permanent rank-based roles.

## Existing implementation gap

The current `src/vidyarthi/governance.py` exposes static academic role names, and the white paper describes an issuer/role workflow. The decisions above supersede that as the target model, but details of capability issuance, delegation, expiry, revocation, issuer authority, and multi-party approvals remain unresolved. Do not claim the capability model is implemented until the open questions are answered and tests demonstrate it.

## Next steps

1. Fill out [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md), especially Q1–Q3 and Q16.
2. Resolve contradictions before altering authorization/credential issuance behavior.
3. Update specification, schemas, code, tests, course content, and changelog together after answers are approved.
