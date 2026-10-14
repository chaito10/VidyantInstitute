"""Signed portable credentials — Vidyarthi §8.

Initial design uses public-key signatures + append-only history (§8.2, §8.4).
A blockchain is DEFERRED — not required for the initial release. Signed
records replicated across peers are the starting point; consensus only if a
demonstrated governance requirement justifies it.

Credential lifecycle (§8.2): eligibility → verification → authorization →
issuance (sign) → distribution → verification → correction/revocation
(append-only; never silently overwrite).

A cryptographically valid credential is NOT automatically a legally
recognized degree (§8.3). UIs must distinguish community-issued,
institution-issued, and legally recognized credentials.

No token / cryptocurrency: academic credits must not be conflated with
tradable financial assets (§8.4).
"""
from __future__ import annotations

import base64
import hashlib
import json
import time
from typing import Any

try:
    from nacl.signing import SigningKey, VerifyKey
    from nacl.exceptions import BadSignatureError
    _BACKEND = "nacl"
except Exception:  # pragma: no cover - e.g. broken cffi on some Pythons
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PrivateKey, Ed25519PublicKey,
        )
        from cryptography.exceptions import InvalidSignature
        _BACKEND = "cryptography"
    except Exception:
        _BACKEND = "hmac-dev"  # stdlib fallback; NOT production-grade pubkey crypto

REQUIRED_CREDENTIAL_FIELDS = (
    "credential_id", "learner", "course_id", "course_revision",
    "outcomes", "issuer", "issuer_authority", "policy",
    "issued_at", "signature",
)

CREDENTIAL_KINDS = ("community", "institution", "legally-recognized")


def generate_issuer_keypair() -> tuple[str, str]:
    """Generate an issuer keypair. Returns (verify_key_b64, signing_key_b64).

    Uses Ed25519 via PyNaCl/cryptography when available; otherwise a stdlib
    HMAC dev fallback (NOT production pubkey crypto — repair cffi/cryptography
    for production use).
    """
    import hmac as _hmac
    import os as _os
    if _BACKEND == "nacl":
        sk = SigningKey.generate()
        return (base64.b64encode(bytes(sk.verify_key)).decode(),
                base64.b64encode(bytes(sk)).decode())
    if _BACKEND == "cryptography":
        sk = Ed25519PrivateKey.generate()
        vk = sk.public_key()
        from cryptography.hazmat.primitives import serialization as _ser
        return (
            base64.b64encode(vk.public_bytes(_ser.Encoding.Raw, _ser.PublicFormat.Raw)).decode(),
            base64.b64encode(sk.private_bytes(_ser.Encoding.Raw, _ser.PrivateFormat.Raw, _ser.NoEncryption())).decode(),
        )
    seed = _os.urandom(32)
    # DEV ONLY: symmetric fallback — verify key == signing key (not pubkey crypto).
    return (base64.b64encode(seed).decode(), base64.b64encode(seed).decode())


def _canonical(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def sign_credential(payload: dict[str, Any], signing_key_b64: str) -> dict[str, Any]:
    """Sign a credential payload. Returns credential dict with 'signature'."""
    import hmac as _hmac
    body = {k: v for k, v in payload.items() if k != "signature"}
    raw = base64.b64decode(signing_key_b64)
    if _BACKEND == "nacl":
        sig = SigningKey(raw).sign(_canonical(body)).signature
        return {**body, "signature": base64.b64encode(sig).decode()}
    if _BACKEND == "cryptography":
        from cryptography.hazmat.primitives import serialization as _ser
        sk = Ed25519PrivateKey.from_private_bytes(raw)
        return {**body, "signature": base64.b64encode(sk.sign(_canonical(body))).decode()}
    sig = _hmac.new(raw, _canonical(body), hashlib.sha256).digest()
    cred = {**body, "signature": base64.b64encode(sig).decode()}
    cred.setdefault("_dev_backend", "hmac-sha256 (not Ed25519 — dev only)")
    return cred


def verify_credential(cred: dict[str, Any], issuer_verify_key_b64: str) -> bool:
    import hmac as _hmac
    sig_b64 = cred.get("signature")
    if not sig_b64:
        return False
    body = {k: v for k, v in cred.items() if k != "signature" and k != "_dev_backend"}
    try:
        if _BACKEND == "nacl":
            VerifyKey(base64.b64decode(issuer_verify_key_b64)).verify(
                _canonical(body), base64.b64decode(sig_b64))
            return True
        if _BACKEND == "cryptography":
            from cryptography.hazmat.primitives import serialization as _ser
            vk = Ed25519PublicKey.from_public_bytes(base64.b64decode(issuer_verify_key_b64))
            vk.verify(base64.b64decode(sig_b64), _canonical(body))
            return True
        # dev fallback cannot verify pubkey-side; recompute only if caller passes
        # the seed as verify key — used only for round-trip tests on broken envs.
        import hmac as _hmac2
        expected = _hmac2.new(base64.b64decode(issuer_verify_key_b64),
                              _canonical(body), hashlib.sha256).digest()
        return _hmac2.compare_digest(expected, base64.b64decode(sig_b64))
    except Exception:
        return False


def build_credential(
    *,
    credential_id: str,
    learner: str,
    course_id: str,
    course_revision: str,
    outcomes: list[str],
    issuer: str,
    issuer_authority: str,
    policy: str,
    kind: str = "community",
    credit: dict[str, Any] | None = None,
    evidence_ref: str = "",
) -> dict[str, Any]:
    if kind not in CREDENTIAL_KINDS:
        raise ValueError(f"kind must be one of {CREDENTIAL_KINDS}")
    return {
        "credential_id": credential_id,
        "learner": learner,
        "course_id": course_id,
        "course_revision": course_revision,
        "outcomes": outcomes,
        "credit": credit or {},
        "evidence_ref": evidence_ref,
        "issuer": issuer,
        "issuer_authority": issuer_authority,
        "policy": policy,
        "kind": kind,  # UI must distinguish community / institution / legally-recognized (§8.3)
        "issued_at": int(time.time()),
        "status": "issued",
        "signature": "",
    }


def validate_credential_shape(cred: dict[str, Any]) -> list[str]:
    return [f"missing required field: {f}" for f in REQUIRED_CREDENTIAL_FIELDS if not cred.get(f)]


class AppendOnlyCredentialLog:
    """Hash-linked, append-only credential history (§8.4 starting point).

    Corrections/revocations are new records, never edits. Note: hash
    chaining alone does not prevent equivocation by a malicious operator —
    readers must compare histories across peers (§8.4).
    """

    def __init__(self) -> None:
        self.records: list[dict[str, Any]] = []

    def append(self, record: dict[str, Any]) -> dict[str, Any]:
        prev = self.records[-1]["record_hash"] if self.records else "GENESIS"
        entry = {
            "prev": prev,
            "record": record,
            "appended_at": int(time.time()),
        }
        entry["record_hash"] = hashlib.sha256(_canonical(entry)).hexdigest()
        self.records.append(entry)
        return entry

    def revoke(self, credential_id: str, reason: str, issuer: str) -> dict[str, Any]:
        return self.append({
            "type": "revocation",
            "credential_id": credential_id,
            "reason": reason,
            "issuer": issuer,
        })

    def verify_chain(self) -> bool:
        prev = "GENESIS"
        for entry in self.records:
            if entry["prev"] != prev:
                return False
            h = hashlib.sha256(_canonical({
                "prev": entry["prev"],
                "record": entry["record"],
                "appended_at": entry["appended_at"],
            })).hexdigest()
            if h != entry["record_hash"]:
                return False
            prev = entry["record_hash"]
        return True
