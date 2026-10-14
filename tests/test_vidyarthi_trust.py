import unittest
from src.vidyarthi.credentials import (
    generate_issuer_keypair, build_credential, sign_credential,
    verify_credential, validate_credential_shape, AppendOnlyCredentialLog,
)
from src.vidyarthi.byok import ProviderConfig, redact
from src.vidyarthi.gamification import LearnerProgress, check_rate_limit


class TestCredentials(unittest.TestCase):
    def test_sign_verify(self):
        vk, sk = generate_issuer_keypair()
        cred = build_credential(
            credential_id="cred-1", learner="learner-pubkey",
            course_id="vidyarthi:cybersecurity:101", course_revision="rev-1",
            outcomes=["Explain fundamental security principles"],
            issuer="issuer-1", issuer_authority="community-board",
            policy="policy-v1", kind="community",
        )
        signed = sign_credential(cred, sk)
        self.assertEqual(validate_credential_shape(signed), [])
        self.assertTrue(verify_credential(signed, vk))
        tampered = dict(signed)
        tampered["outcomes"] = ["forged"]
        self.assertFalse(verify_credential(tampered, vk))

    def test_append_only_log(self):
        log = AppendOnlyCredentialLog()
        log.append({"type": "issuance", "credential_id": "c1"})
        log.revoke("c1", "test", "issuer-1")
        self.assertTrue(log.verify_chain())
        self.assertEqual(len(log.records), 2)


class TestBYOK(unittest.TestCase):
    def test_local_disclosure(self):
        cfg = ProviderConfig(kind="ollama", endpoint="http://localhost:11434", local=True)
        self.assertEqual(cfg.validate(), [])
        self.assertIn("local", cfg.disclosure())

    def test_remote_disclosure(self):
        cfg = ProviderConfig(kind="hosted", endpoint="https://api.example.com", local=False)
        self.assertIn("remote", cfg.disclosure())

    def test_redact(self):
        self.assertEqual(redact("key=abc123", ["abc123"]), "key=***REDACTED***")


class TestGamification(unittest.TestCase):
    def test_xp_not_competency(self):
        p = LearnerProgress()
        p.award_xp(10)
        self.assertEqual(p.xp, 10)
        self.assertEqual(p.competency, {})
        p.record_competency("o1", 95, "evidence-1")
        self.assertIn("o1", p.competency)

    def test_rate_limit(self):
        self.assertTrue(check_rate_limit(5))
        self.assertFalse(check_rate_limit(999))


if __name__ == "__main__":
    unittest.main()
