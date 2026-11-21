"""
DAY 10 LESSON — Safe Dict Access & Iteration Traps (Easy -> Advanced -> Industrial)
Run: python day-10/lesson.py

ANALOGY: `.get(key, default)` is knocking politely; `d[key]` kicks the door down
         and crashes if nobody is home (`KeyError`).
WHEN TO USE:     `.get()` for optional keys; `defaultdict(list)` for grouping items.
WHEN NOT TO USE: Never add/delete keys inside `for k in my_dict:`!
JS BRIDGE:       Python `d.get("k", 0)` == JS `obj.k ?? 0`
"""
from collections import defaultdict


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
inventory = {"potion": 3, "iron": 5}
print("Potions:", inventory.get("potion", 0))
print("Arrows (missing):", inventory.get("arrow", 0))
# .setdefault(k, val): gets k if present, otherwise sets inventory[k] = val!
inventory.setdefault("shield", 1)
print("After setdefault:", inventory)

for item, qty in inventory.items():
    print(f"  - {item}: {qty}")


# =========================================================
# LEVEL 2: ADVANCED MODE (defaultdict & Iteration Trap)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# 1. Grouping items: Junior `if k not in d: d[k] = []` vs Senior `defaultdict(list)`
grouped: dict[str, list[str]] = defaultdict(list)
for role, name in [("ai", "Zack"), ("backend", "Ali"), ("ai", "Sara")]:
    grouped[role].append(name)
print("Grouped:", dict(grouped))

# 2. Dict Comprehension filtering (avoids RuntimeError when deleting while looping!)
scores = {"a": 10, "b": 0, "c": 25}
cleaned = {k: v for k, v in scores.items() if v > 0}
print("Filtered:", cleaned)

# TRY BREAKING IT (uncomment next line to see KeyError):
# _ = inventory["arrow"]


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: Grouping RAG Search Results by Source Document]

def group_chunks_by_doc(chunks: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Groups `(doc_id, text_chunk)` pairs into `{doc_id: [chunks...]}`."""
    by_doc: dict[str, list[str]] = defaultdict(list)
    for doc_id, text in chunks:
        by_doc[doc_id].append(text)
    return dict(by_doc)

sample_chunks = [("guide.pdf", "Intro"), ("faq.md", "Q1"), ("guide.pdf", "Setup")]
print("Grouped docs:", group_chunks_by_doc(sample_chunks))

# FEYNMAN CHECK (answer in 1 sentence):
# -> When should you use `d.get(key, default)` instead of `d[key]`?
