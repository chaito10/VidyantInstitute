"""BYOK AI provider adapters — Vidyarthi §4.

No single centrally funded provider (§4.1). Learners configure their own
provider + credentials. Supported (§4.1): hosted APIs, OpenAI-compatible
endpoints, local servers (Ollama / llama.cpp), institution gateways,
community adapters. Capabilities (streaming, tools, multimodal, structured
output) are OPTIONAL — never assume them.

Key rules (§4.2):
- keys in memory by default; persist only on explicit opt-in + encryption
- never write keys to repos, share across peers, embed in assets, or log them
- disclose local vs remote inference before transmitting data
- never silently proxy user keys through a shared backend; direct
  browser→provider may fail on CORS/auth → use explicit local/institutional
  gateway instead
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

SUPPORTED_PROVIDER_KINDS = (
    "hosted",
    "openai-compatible",
    "ollama",
    "llamacpp",
    "institutional-gateway",
    "community-adapter",
)


@dataclass
class ProviderConfig:
    kind: str
    endpoint: str
    model: str = ""
    # NOTE: api_key lives in memory only. Do not serialize to course repos.
    api_key: str = field(default="", repr=False)
    local: bool = False  # True => inference stays on device/network

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.kind not in SUPPORTED_PROVIDER_KINDS:
            errors.append(f"unsupported provider kind: {self.kind!r}")
        if not self.endpoint:
            errors.append("endpoint is required (explicit gateway, never silent proxy)")
        if self.kind in ("hosted", "openai-compatible", "institutional-gateway") and not self.local:
            pass  # remote — caller must disclose data transfer (§4.2)
        return errors

    def disclosure(self) -> str:
        if self.local or self.kind in ("ollama", "llamacpp"):
            return "local inference — prompts stay on your device/network"
        return f"remote inference — prompts will be sent to {self.endpoint} (kind={self.kind})"


def redact(text: str, secrets: list[str]) -> str:
    """Redact secret values from logs / diagnostics (§4.2)."""
    out = text
    for s in secrets:
        if s:
            out = out.replace(s, "***REDACTED***")
    return out


def build_tutor_messages(course_context: str, learner_prompt: str, history: list[dict[str, str]] | None = None) -> list[dict[str, str]]:
    """Build tutor messages grounded in the active course (§4.4).

    The tutor must cite source lessons where possible and must not invent
    citations or present unverified answers as authoritative.
    """
    system = (
        "You are a Vidyarthi course tutor. Use ONLY the provided course context as "
        "primary ground truth. Cite source lesson IDs. Distinguish grounded facts from "
        "generated suggestions. Never invent citations. Offer hints before solutions."
    )
    messages = [{"role": "system", "content": system}]
    if course_context:
        messages.append({"role": "system", "content": f"COURSE CONTEXT:\n{course_context}"})
    messages.extend(history or [])
    messages.append({"role": "user", "content": learner_prompt})
    return messages


def generation_stages() -> list[str]:
    """AI course-generation pipeline stages (§4.3)."""
    return [
        "1-curriculum-planning",
        "2-learning-content",
        "3-presentation-marp",
        "4-assessment-generation",
        "5-multimedia-scripts",
        "6-validation",
        "7-human-review-publication",
    ]
