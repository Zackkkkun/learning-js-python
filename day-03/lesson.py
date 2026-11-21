"""
DAY 03 LESSON — Functions, Error Handling, Custom Exceptions & File I/O
Run: python day-03/lesson.py
"""

# 1. Safe Division with try/except
print("--- 1. ERROR HANDLING ---")
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Edge case: cannot divide by zero!")
        return None

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

# 2. Custom Exceptions
print("\n--- 2. CUSTOM EXCEPTIONS ---")
class NegativeScoreError(Exception):
    pass

def set_score(val: int) -> int:
    if val < 0:
        raise NegativeScoreError("Score cannot be negative!")
    return val

try:
    set_score(-5)
except NegativeScoreError as err:
    print("Caught custom error:", err)

# 3. File I/O (context manager `with` auto-closes the file)
print("\n--- 3. FILE I/O ---")
from pathlib import Path
sample = Path("day-03/_lesson_sample.txt")
sample.write_text("Line 1: Python File I/O\n", encoding="utf-8")
print("Read from file:", sample.read_text(encoding="utf-8").strip())
sample.unlink()  # Clean up temp file
