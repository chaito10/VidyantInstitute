import unittest
from src.vidyarthi.governance import ROLES, can, is_authorized_issuer
from src.vidyarthi.sync import strategy_for, merge_records


class TestGovernance(unittest.TestCase):
    def test_seven_roles(self):
        self.assertEqual(len(ROLES), 7)
        self.assertIn("credential-issuer", ROLES)

    def test_scoped_permissions(self):
        self.assertTrue(can("learner", "study"))
        self.assertTrue(can("assessment-operator", "sign-result"))
        self.assertFalse(can("learner", "issue-credential"))
        self.assertFalse(can("learner", "mint-token"))
        self.assertFalse(can("unknown-role", "study"))

    def test_issuer_authorization(self):
        self.assertTrue(is_authorized_issuer("credential-issuer", "community"))
        self.assertTrue(is_authorized_issuer("credential-issuer", "institution"))
        self.assertFalse(is_authorized_issuer("learner", "community"))
        self.assertFalse(is_authorized_issuer("credential-issuer", "token-holder"))


class TestSync(unittest.TestCase):
    def test_strategies(self):
        self.assertEqual(strategy_for("course-content"), "repository-history-merge")
        self.assertEqual(strategy_for("credential"), "verify-signed-record-no-merge")
        with self.assertRaises(ValueError):
            strategy_for("token-balance")

    def test_discussion_union_ordered(self):
        local = [{"id": "m1", "timestamp": 2}]
        remote = [{"id": "m1", "timestamp": 2}, {"id": "m2", "timestamp": 1}]
        merged = merge_records("discussion", local, remote)
        self.assertEqual([m["id"] for m in merged], ["m2", "m1"])

    def test_no_last_write_wins_for_credentials(self):
        local = [{"credential_id": "c1"}]
        remote = [{"credential_id": "c2-evil"}]
        self.assertEqual(merge_records("credential", local, remote), local)

    def test_progress_explicit_rules(self):
        local = [{"outcome_id": "o1", "event_id": "e1", "timestamp": 1}]
        remote = [{"outcome_id": "o1", "event_id": "e2", "timestamp": 2}]
        merged = merge_records("learner-progress", local, remote)
        self.assertEqual(merged[0]["event_id"], "e2")


if __name__ == "__main__":
    unittest.main()
