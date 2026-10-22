# Apply these VidyantInstitute updates

The GitHub connector allowed repository inspection but rejected write operations, and a direct clone was unavailable in this runtime. These changes therefore have **not** been committed to GitHub.

From a local clone of `chaito10/VidyantInstitute`, copy `VidyantInstitute-decisions.patch` into the repository root and run:

```bash
git switch -c docs/vidyarthi-decisions
git apply --check VidyantInstitute-decisions.patch
git apply VidyantInstitute-decisions.patch
git diff --check
git diff --stat
```

Review the changes, run the repository's tests, then commit and push the branch or open a pull request. The patch updates `README.md` and `white_paper.md`, and adds `docs/PROJECT_DECISIONS.md` plus `docs/OPEN_QUESTIONS.md`.

The authorization implementation in `src/vidyarthi/governance.py` is intentionally not rewritten in this pass: the flat participant direction is confirmed, but capability grant/delegation/expiry/revocation semantics remain unanswered and must not be guessed.
