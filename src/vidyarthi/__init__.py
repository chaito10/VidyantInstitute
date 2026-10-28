"""Vidyarthi core package.

Implements the portable application-level schemas and helpers for:
- course manifest validation (§3)
- assessment job / result handling (§5)
- signed portable credentials, no blockchain required (§8)
- BYOK AI provider adapters (§4)
- gamification with XP separated from competency (§7)

Design: local-first, repository-native, provider-independent, composable,
open/inspectable, evidence-based, portable, resource-efficient.
"""

__version__ = "0.3.0"
SPEC_VERSION = "Vidyarthi v0.3 (2026-10-22)"
