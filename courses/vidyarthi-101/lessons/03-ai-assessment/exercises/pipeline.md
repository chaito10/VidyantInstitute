# Exercise — run the assessment pipeline

1. Run `python scripts/run_assessment.py --job courses/vidyarthi-101/assessments/tests/basic.json`
   and inspect the JSON report: find `limits.network`, `grading_rationale`,
   and `signing_identity`.
2. Explain why `signing_identity` reads `unauthorized-local-preview` — which
   pipeline stage (§5.2) is missing, and who performs it?
3. In `public/vidyarthi.html`, open §3 (BYOK) and describe what happens to the
   key field when you press "Set provider".
