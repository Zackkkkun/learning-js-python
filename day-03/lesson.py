"""
DAY 03 LESSON (ADVANCED DEPTH) — Exceptions (try/except/else/finally) & File I/O
Run: python day-03/lesson.py
"""
from pathlib import Path

# =========================================================
# 1. FULL EXCEPTION FLOW (TRY / EXCEPT / ELSE / FINALLY)
# =========================================================
print("--- 1. TRY / EXCEPT / ELSE / FINALLY ---")
def parse_positive(raw: str) -> int | None:
    try:
        num = int(raw)
        if num <= 0:
            raise ValueError("Must be > 0")
    except ValueError as err:
        print(f"Rejected {raw!r}: {err}")
        return None
    else:
        print(f"Parsed cleanly: {num}")  # Runs ONLY if try succeeded
        return num
    finally:
        pass  # Always runs (ideal for closing DB/network resources)

parse_positive("42")
parse_positive("-5")


# =========================================================
# 2. CUSTOM DOMAIN EXCEPTIONS
# =========================================================
print("\n--- 2. CUSTOM EXCEPTIONS ---")
class InsufficientXP(Exception):
    pass

def unlock_boss(xp: int) -> str:
    if xp < 1000:
        raise InsufficientXP(f"Need 1000 XP, have {xp}")
    return "Boss Unlocked!"

try:
    unlock_boss(400)
except InsufficientXP as err:
    print("Domain error:", err)


# =========================================================
# 3. SAFE FILE I/O WITH PATHLIB & UTF-8
# =========================================================
print("\n--- 3. FILE I/O & ENCODING ---")
sample = Path("day-03/_lesson_sample.txt")
sample.write_text("Line 1: UTF-8 safe ✓\n", encoding="utf-8")
print("Read:", sample.read_text(encoding="utf-8").strip())
sample.unlink()
