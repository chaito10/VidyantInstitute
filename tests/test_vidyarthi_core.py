import unittest
from src.vidyarthi.course import validate_course_manifest, validate_course_dir
from src.vidyarthi.assessment import validate_job, build_result_report, apply_rubric


class TestCourse(unittest.TestCase):
    def test_valid_manifest(self):
        data = {
            "schema_version": "1.0",
            "id": "vidyarthi:cybersecurity:101",
            "title": "Foundations of Cybersecurity",
            "version": "1.0.0",
            "language": "en",
            "credits": {"value": 2, "system": "vidyarthi-proposed"},
            "modules": [{"id": "security-fundamentals", "path": "lessons/01-foundations"}],
        }
        self.assertEqual(validate_course_manifest(data), [])

    def test_invalid_manifest(self):
        self.assertTrue(validate_course_manifest({}))

    def test_example_course_dir(self):
        self.assertEqual(validate_course_dir("courses/cybersecurity-101"), [])


class TestAssessment(unittest.TestCase):
    def test_job_example(self):
        job = {
            "schema_version": "1.0",
            "job_id": "job-001",
            "course_id": "vidyarthi:cybersecurity:101",
            "course_revision": "approved-revision-id",
            "submission_id": "submission-001",
            "runner": "wasm",
            "tests": ["assessments/tests/basic.json"],
            "limits": {"timeout_seconds": 30, "memory_mb": 128, "network": False},
        }
        self.assertEqual(validate_job(job), [])

    def test_network_must_be_denied(self):
        job = {
            "schema_version": "1.0", "job_id": "j", "course_id": "c",
            "course_revision": "r", "submission_id": "s",
            "runner": "wasm", "tests": ["t"],
            "limits": {"network": True},
        }
        self.assertTrue(any("network" in e for e in validate_job(job)))

    def test_rubric(self):
        score, rationale = apply_rubric(
            [{"name": "a", "passed": True}, {"name": "b", "passed": False}],
            {"weights": {"a": 1.0, "b": 1.0}, "pass_threshold": 60},
        )
        self.assertEqual(score, 50.0)
        self.assertIn("FAIL", rationale)

    def test_report_fields(self):
        rep = build_result_report(
            submission_bytes=b"demo", course_revision="r", test_version="t",
            rubric_version="rb", runner="wasm", runtime_version="v",
            limits=None, test_outcomes=[{"name": "a", "passed": True}],
            rubric={"weights": {"a": 1}, "pass_threshold": 60},
        )
        for f in ("submission_hash", "score", "grading_rationale", "timestamp"):
            self.assertIn(f, rep)


if __name__ == "__main__":
    unittest.main()
