"""`python -m src` — Vidyarthi entrypoint (see main.py)."""
from main import main as _main
import sys as _sys

if __name__ == "__main__":
    raise SystemExit(_main(["main.py", * _sys.argv[1:]]))
