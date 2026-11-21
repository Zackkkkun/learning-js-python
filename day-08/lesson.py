"""
DAY 08 LESSON (ADVANCED DEPTH) — Shallow vs Deep Copy & Safe Aggregation
Run: python day-08/lesson.py
"""
import copy

# =========================================================
# 1. SAFE AGGREGATION (EMPTY INPUT GUARD)
# =========================================================
print("--- 1. SAFE AGGREGATION ---")
def get_average(scores: list[int]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

print("Avg [80, 90, 100]:", get_average([80, 90, 100]))
print("Avg []:", get_average([]))


# =========================================================
# 2. SHALLOW COPY vs DEEP COPY (NESTED DATA TRAP!)
# =========================================================
print("\n--- 2. SHALLOW vs DEEP COPY ---")
team = [["Zack", 100], ["Sara", 95]]

shallow = team.copy()
shallow[0][1] = 0  # Mutates the INNER list inside `team` too!
print("Original after shallow edit:", team)

team = [["Zack", 100], ["Sara", 95]]
deep = copy.deepcopy(team)
deep[0][1] = 0     # Completely isolated!
print("Original after deep edit:", team)
print("Deep copy:", deep)
