"""Governance roles and issuer authorization — Vidyarthi §11.1.

Roles: learners, course authors, course reviewers, assessment operators,
credential issuers, network maintainers, community moderators. One
participant may hold several roles, but permissions stay explicitly scoped.

There is deliberately NO token-weighted voting here: curriculum updates,
credential issuance, and contributor recognition follow published academic
rules and scoped permissions, not coin holdings (§8.4, §11).
"""
from __future__ import annotations

ROLES = (
    "learner",
    "course-author",
    "course-reviewer",
    "assessment-operator",
    "credential-issuer",
    "network-maintainer",
    "community-moderator",
)

# Which role may perform which action. Scoped explicitly (§11.1).
PERMISSIONS: dict[str, frozenset[str]] = {
    "learner": frozenset({"study", "submit", "discuss", "export-own-data"}),
    "course-author": frozenset({"create-course", "edit-draft", "propose-release"}),
    "course-reviewer": frozenset({"review-course", "approve-assessment-design"}),
    "assessment-operator": frozenset({"run-assessment-job", "sign-result"}),
    "credential-issuer": frozenset({"issue-credential", "revoke-credential"}),
    "network-maintainer": frozenset({"maintain-software", "maintain-protocol"}),
    "community-moderator": frozenset({"moderate-discussion", "report-abuse"}),
}


def can(role: str, action: str) -> bool:
    """Check whether a role is authorized for an action."""
    return action in PERMISSIONS.get(role, frozenset())


def is_authorized_issuer(role: str, credential_kind: str) -> bool:
    """Only the credential-issuer role may issue; the kind (community /
    institution / legally-recognized, §8.3) must additionally match a
    published credit policy — checked by the degree engine, not here."""
    if role != "credential-issuer":
        return False
    return credential_kind in ("community", "institution", "legally-recognized")
