# Vidyarthi — local validation image (optional; deployments are local-first, §9.3).
FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY schemas/ ./schemas/
COPY courses/ ./courses/
COPY scripts/ ./scripts/
COPY main.py ./
RUN python -m compileall src main.py scripts \
 && python scripts/validate_course.py courses/cybersecurity-101
CMD ["python", "main.py", "info"]
