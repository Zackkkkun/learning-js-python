"""
DAY 10 LESSON (ADVANCED DEPTH) — Dict Internals, Safe Access & Mutation Trap
Run: python day-10/lesson.py
"""
from collections import defaultdict

# =========================================================
# 1. SAFE LOOKUP: .get() vs .setdefault() vs defaultdict
# =========================================================
print("--- 1. SAFE DICT PATTERNS ---")
inventory = {"potion": 3, "iron": 5}
print("Arrows (safe):", inventory.get("arrow", 0))

# Grouping items cleanly with defaultdict(list):
grouped: dict[str, list[str]] = defaultdict(list)
for role, name in [("ai", "Zack"), ("backend", "Ali"), ("ai", "Sara")]:
    grouped[role].append(name)
print("Grouped:", dict(grouped))


# =========================================================
# 2. EDGE CASE: MUTATING A DICT WHILE ITERATING
# =========================================================
print("\n--- 2. ITERATION MUTATION TRAP ---")
scores = {"a": 10, "b": 0, "c": 25}

# Never delete keys directly while looping over `scores`!
# Iterate over `list(scores.keys())` or build a new dict:
cleaned = {k: v for k, v in scores.items() if v > 0}
print("Filtered dict:", cleaned)
