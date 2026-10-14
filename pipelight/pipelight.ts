// Pipelight pipeline — Vidyarthi §5 (TypeScript, Pipelight v2+).
// Validates the course package then runs a restricted assessment job.
// This file declares CI orchestration; the portable application schema lives
// in schemas/assessment-job.schema.json and is translated by scripts/run_assessment.py.
import { pipeline, step } from "pipelight";

pipeline("vidyarthi-validate", {
  triggers: [{ branches: ["main"] }],
  steps: [
    step("validate-course", { run: "python scripts/validate_course.py courses/cybersecurity-101" }),
    step("run-assessment", { run: "python scripts/run_assessment.py --job courses/cybersecurity-101/assessments/tests/basic.json" }),
  ],
});
