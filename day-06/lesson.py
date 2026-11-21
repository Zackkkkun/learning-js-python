"""
DAY 06 LESSON — Loops, Filtering & Accumulators
Run: python day-06/lesson.py
"""

print("--- FILTER & ACCUMULATE ---")
scores = [45, 82, 91, 60, 38, 77]

passed = []
for s in scores:
    if s >= 60:
        passed.append(s)

print("All scores:", scores)
print("Passed (>=60):", passed)
print("Pass count:", len(passed))
