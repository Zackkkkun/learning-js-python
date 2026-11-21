"""
DAY 03 LESSON — Exceptions & File I/O (Easy -> Advanced -> Industrial)
Run: python day-03/lesson.py

ANALOGY: `try/except` is an airbag; `finally` is the cleanup crew that always shows up.
WHEN TO USE:     Catch specific errors (`ValueError`, `FileNotFoundError`) on risky I/O/input.
WHEN NOT TO USE: Never write bare `except:` — it hides typos and blocks Ctrl+C!
JS BRIDGE:       Python `try/except/finally` == JS `try/catch/finally`
"""
from pathlib import Path


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
try:
    num = int("not_a_number")
except ValueError:
    print("Caught bad number cleanly!")

# PREDICT BEFORE RUNNING: Does `else` run when `try` raises an error?
try:
    _ = 10 / 2
except ZeroDivisionError:
    print("Divided by zero!")
else:
    print("PREDICT: Division succeeded!")


# =========================================================
# LEVEL 2: ADVANCED MODE (Custom Exceptions & Safe Files)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   context manager (`with`) = auto-closes files/connections even if an error happens

class InsufficientXP(Exception):
    """Custom domain error for business rules."""

def unlock_boss(xp: int) -> str:
    if xp < 1000:
        raise InsufficientXP(f"Need 1000 XP, have {xp}")
    return "Boss Unlocked!"

try:
    unlock_boss(400)
except InsufficientXP as err:
    print("Domain error:", err)

# Safe UTF-8 file write/read with pathlib
tmp = Path("day-03/_lesson_tmp.txt")
tmp.write_text("UTF-8 safe ✓\n", encoding="utf-8")
print("File content:", tmp.read_text(encoding="utf-8").strip())
tmp.unlink()

# TRY BREAKING IT (uncomment next line to see FileNotFoundError):
# Path("does_not_exist.txt").read_text()


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: Loading Configs/Prompts Safely in FastAPI & AI Pipelines]

def load_prompt_file(path: str, fallback: str = "Default system prompt.") -> str:
    """Reads a prompt template safely without crashing the server if missing."""
    try:
        return Path(path).read_text(encoding="utf-8").strip()
    except OSError:
        return fallback

print("Prompt:", load_prompt_file("missing_prompt.txt"))

# FEYNMAN CHECK (answer in 1 sentence):
# -> Why is `except ValueError:` much safer than a bare `except:`?
