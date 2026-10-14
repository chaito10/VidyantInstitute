"""Vidyarthi core package — implements Vidyarthi White Paper v0.1 (11 Oct 2026).

Source of truth: Vidyarthi_White_Paper.docx at repo root
(Project: Vidyarthi — Digital Distributed University, status: Proposed architecture).

This package provides the minimal application-level schemas and helpers for:
- course manifest validation (§3)
- assessment job / result handling (§5)
- signed portable credentials, no blockchain required (§8)
- BYOK AI provider adapters (§4)
- gamification with XP separated from competency (§7)

Design notes (§1.3): local-first, repository-native, provider-independent,
composable, open/inspectable, evidence-based, portable, resource-efficient.
"""

__version__ = "0.1.0"
SPEC_VERSION = "Vidyarthi White Paper v0.1 (2026-10-11)"
