"""
DAY 09 LESSON (ADVANCED DEPTH) — Dictionaries, Hashing & Counting Patterns
Run: python day-09/lesson.py
"""
from collections import Counter

# =========================================================
# 1. DICTIONARIES AS O(1) HASH MAPS
# =========================================================
print("--- 1. DICT MERGING & DEFAULTS ---")
defaults = {"theme": "dark", "xp_rate": 1.0}
overrides = {"xp_rate": 1.5, "rank": "D-Rank"}

# Python 3.9+ clean merge operator (|): right side wins on conflicts
config = defaults | overrides
print("Merged config:", config)


# =========================================================
# 2. COUNTING & FREQUENCY MAPS
# =========================================================
print("\n--- 2. FREQUENCY COUNTING ---")
logs = ["login", "quest", "quest", "push", "quest"]

# Manual pattern with .get():
counts: dict[str, int] = {}
for event in logs:
    counts[event] = counts.get(event, 0) + 1
print("Manual counts:", counts)

# Senior stdlib shortcut (Counter):
print("Counter:", Counter(logs).most_common(2))
