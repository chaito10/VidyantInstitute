"""Gamification — Vidyarthi §7.

Separate engagement, contribution quality, and demonstrated competency.
Table 1 mapping:
- XP → activity/progress (NOT competence)
- levels/badges → milestones (NOT qualifications)
- streaks → regularity (NOT quality)
- reputation → useful contributors (NOT formal expertise)
- competency records → demonstrated outcomes (NOT auto-degree)
- academic credits → policy-bound achievement (NOT universal recognition)

Gamification metrics must never be presented as academic mastery (§13).
Anti-gaming (§7.3): rate limits, randomized variants, independent reviewers,
evidence requirements, anomaly detection, periodic reassessment.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LearnerProgress:
    xp: int = 0
    streak_days: int = 0
    badges: list[str] = field(default_factory=list)
    # competency: outcome_id -> {score, evidence_ref}
    competency: dict[str, dict] = field(default_factory=dict)
    reputation: int = 0

    def award_xp(self, amount: int, reason: str = "") -> int:
        if amount < 0:
            raise ValueError("XP awards must be non-negative (no single score gates education, §7.3)")
        self.xp += amount
        return self.xp

    def record_competency(self, outcome_id: str, score: float, evidence_ref: str) -> None:
        """Competency is evidence-bound and independent of XP (§7.2)."""
        self.competency[outcome_id] = {"score": score, "evidence_ref": evidence_ref}

    def summary(self) -> dict:
        return {
            "xp": self.xp,  # engagement only — not competence
            "streak_days": self.streak_days,
            "badges": list(self.badges),
            "competency": dict(self.competency),
            "reputation": self.reputation,
        }


def check_rate_limit(actions_last_minute: int, limit: int = 20) -> bool:
    """True if within limit. Used against automated farming (§7.3)."""
    return actions_last_minute <= limit
