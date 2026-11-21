"""
DAY 09 LESSON — Dictionaries, Merging & Counting (Easy -> Advanced -> Industrial)
Run: python day-09/lesson.py

ANALOGY: A dictionary is a real-world phonebook: look up a name (key) and jump
         straight to the number (value) without reading every page.
WHEN TO USE:     Key-value mapping, fast O(1) lookup, counting frequencies.
WHEN NOT TO USE: Don't use a list of pairs when you need fast lookup by ID/name.
JS BRIDGE:       Python `defaults | overrides` == JS `{...defaults, ...overrides}`
"""
from collections import Counter


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
student = {"name": "Zack", "phase": 2, "xp": 1600}
student["xp"] += 100
student["rank"] = "D-Rank"

# Core Dictionary Operations:
#   .keys()    -> all keys        .values() -> all values
#   .items()   -> (key, value)    .update() -> merge/overwrite multiple keys
#   .pop(k, d) -> remove & return (safe with default `d`)
#   k in dict  -> O(1) key check
student.update({"streak": 2, "active": True})
removed = student.pop("missing_key", None)
print("Keys:", list(student.keys()), "| Values:", list(student.values()))
print("Student:", student, "| Safe pop:", removed)


# =========================================================
# LEVEL 2: ADVANCED MODE (Merge Operator & Counting)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   O(1) = instant lookup via hash table regardless of dict size

defaults = {"theme": "dark", "xp_rate": 1.0}
overrides = {"xp_rate": 1.5, "rank": "D-Rank"}
config = defaults | overrides  # Right side wins on duplicate keys
print("Merged:", config)

# Junior vs Senior frequency counting:
logs = ["login", "quest", "quest", "push", "quest"]
# Junior: if k in counts: counts[k] += 1 else: counts[k] = 1
# Senior:
print("Counter:", Counter(logs).most_common(2))


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: API Analytics & LLM Token Usage Tracking]

def summarize_events(events: list[str]) -> dict[str, int]:
    """Counts event frequencies cleanly using collections.Counter."""
    return dict(Counter(e.strip().lower() for e in events if e.strip()))

print("Event summary:", summarize_events([" Login ", "QUEST", "login", " "]))

# FEYNMAN CHECK (answer in 1 sentence):
# -> Why is looking up a user by ID in a `dict` much faster than searching a `list`?
