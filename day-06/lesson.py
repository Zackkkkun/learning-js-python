"""
DAY 06 LESSON (ADVANCED DEPTH) — Filtering, any()/all() & Generator Expressions
Run: python day-06/lesson.py
"""

# =========================================================
# 1. PYTHONIC FILTERING & ACCUMULATION
# =========================================================
print("--- 1. FILTER & AGGREGATE ---")
scores = [45, 82, 91, 60, 38, 77]
passed = [s for s in scores if s >= 60]
print("Passed:", passed, "| Average:", round(sum(passed) / len(passed), 1))


# =========================================================
# 2. ANY() & ALL() (SHORT-CIRCUIT CHECKS)
# =========================================================
print("\n--- 2. ANY() & ALL() ---")
# Much cleaner and faster than manual boolean flag loops!
print("Everyone passed?:", all(s >= 60 for s in scores))
print("Anyone got 90+?:", any(s >= 90 for s in scores))


# =========================================================
# 3. EDGE CASE: EMPTY LISTS IN SUM/AVG/ALL
# =========================================================
print("\n--- 3. EMPTY LIST EDGE CASES ---")
empty: list[int] = []
print("sum([]):", sum(empty))       # 0
print("all([]):", all(empty))       # True! (vacuous truth — watch out!)
print("any([]):", any(empty))       # False
