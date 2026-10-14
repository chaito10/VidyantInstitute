#!/usr/bin/env python3
"""Build the GitHub Pages site (Vidyarthi docs + micro-courses + live client).

Reads white_paper.md, README.md, courses/*/ (syllabus, lessons, quizzes),
schemas/*.json and public/vidyarthi.html; writes static HTML into site/.

Requires: pip install markdown
Usage: python scripts/build_pages.py [--out site]
"""
import html
import json
import shutil
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("pip install markdown  (required to build the Pages site)")

ROOT = Path(__file__).resolve().parent.parent

CSS = """<style>
:root{color-scheme:light dark}body{font-family:system-ui,sans-serif;max-width:860px;margin:2rem auto;padding:0 1rem;line-height:1.6}
nav{border-bottom:1px solid #8884;margin-bottom:1.5rem;padding-bottom:.5rem}nav a{margin-right:1rem}
table{border-collapse:collapse;width:100%}th,td{border:1px solid #8884;padding:.4rem .6rem;text-align:left}
code{background:#8882;padding:.1rem .3rem;border-radius:4px}pre{background:#8882;padding:1rem;border-radius:8px;overflow-x:auto}
.card{border:1px solid #8884;border-radius:12px;padding:1rem;margin:1rem 0}.muted{opacity:.75}
</style>"""

TEMPLATE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title} — Vidyarthi</title>{css}</head><body>
<nav><a href="{root}index.html">Vidyarthi</a><a href="{root}whitepaper.html">Whitepaper</a><a href="{root}courses/index.html">Courses</a><a href="{root}client/index.html">Live client</a><a href="https://github.com/charudatta10/VidyantInstitute">GitHub</a></nav>
{body}</body></html>"""


def md_to_html(path: Path) -> str:
    return markdown.markdown(path.read_text(encoding="utf-8"),
                             extensions=["fenced_code", "tables", "toc"])


def page(title: str, body: str, root: str = "") -> str:
    return TEMPLATE.format(title=html.escape(title), css=CSS, root=root, body=body)


def build(out: Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    (out / "courses").mkdir(parents=True)
    (out / "client").mkdir(parents=True)
    (out / "schemas").mkdir(parents=True)

    # Home
    body = md_to_html(ROOT / "README.md")
    body += ("<div class='card'><h2>Try it</h2>"
             "<p><a href='client/index.html'><b>Open the live learning client</b></a> "
             "(single-file HTML5 app, §9.1) — load a course.json + quiz.json below.</p></div>")
    (out / "index.html").write_text(page("Digital Distributed University", body), encoding="utf-8")

    # Whitepaper
    (out / "whitepaper.html").write_text(
        page("Whitepaper v0.1", md_to_html(ROOT / "white_paper.md")), encoding="utf-8")

    # Client demo (copy as-is)
    shutil.copy(ROOT / "public" / "vidyarthi.html", out / "client" / "index.html")

    # Schemas (raw JSON for reference)
    for schema in (ROOT / "schemas").glob("*.json"):
        shutil.copy(schema, out / "schemas" / schema.name)

    # Courses index + per-course pages
    cards = []
    for course_dir in sorted((ROOT / "courses").iterdir()):
        manifest = course_dir / "course.json"
        if not manifest.exists():
            continue
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        cid = meta.get("id", course_dir.name)
        title = meta.get("title", course_dir.name)
        cards.append(f"<div class='card'><h2><a href='{course_dir.name}/index.html'>{html.escape(title)}</a></h2>"
                     f"<p class='muted'><code>{html.escape(cid)}</code> v{html.escape(str(meta.get('version', '')))}</p></div>")
        cdir = out / "courses" / course_dir.name
        cdir.mkdir(parents=True, exist_ok=True)
        cbody = md_to_html(course_dir / "syllabus.md") if (course_dir / "syllabus.md").exists() else f"<h1>{html.escape(title)}</h1>"
        # lesson links
        lessons = sorted((course_dir / "lessons").iterdir()) if (course_dir / "lessons").exists() else []
        if lessons:
            cbody += "<h2>Lessons</h2><ul>" + "".join(
                f"<li><a href='{l.name}.html'>{html.escape(l.name)}</a></li>" for l in lessons if l.is_dir()) + "</ul>"
        cbody += (f"<p><a href='course.json'>course.json</a> · "
                  f"<a href='https://github.com/charudatta10/VidyantInstitute/tree/main/courses/{course_dir.name}'>source on GitHub</a></p>")
        (cdir / "index.html").write_text(page(title, cbody, root="../../"), encoding="utf-8")
        shutil.copy(manifest, cdir / "course.json")
        for lesson in lessons:
            if not lesson.is_dir():
                continue
            lbody = md_to_html(lesson / "lesson.md") if (lesson / "lesson.md").exists() else f"<h1>{html.escape(lesson.name)}</h1>"
            if (lesson / "quiz.json").exists():
                quiz = json.loads((lesson / "quiz.json").read_text(encoding="utf-8"))
                lbody += "<h2>Quiz preview</h2><ol>" + "".join(
                    f"<li>{html.escape(q.get('prompt', q.get('id', '?')))}</li>"
                    for q in quiz.get("questions", [])) + "</ol>"
                lbody += "<p class='muted'>Full quiz with answer keys: load the course's <code>quiz.json</code> in the live client.</p>"
            (cdir / f"{lesson.name}.html").write_text(page(f"{title} — {lesson.name}", lbody, root="../../"), encoding="utf-8")
    (out / "courses" / "index.html").write_text(
        page("Courses", "<h1>Micro-courses</h1>" + "".join(cards), root="../"), encoding="utf-8")

    print(f"Pages site built: {out} ({sum(1 for _ in out.rglob('*'))} files)")


if __name__ == "__main__":
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[1] == "--out" else Path("site")
    build(ROOT / out_dir if not out_dir.is_absolute() else out_dir)
