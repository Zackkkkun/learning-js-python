"""
DAY 08 LESSON — Integrated Phase 1 Patterns (Lists + Functions + Exceptions)
Run: python day-08/lesson.py
"""

print("--- PHASE 1 INTEGRATION ---")
def get_average(scores: list[int]) -> float:
    if not scores:  # Edge case: empty list avoids ZeroDivisionError
        return 0.0
    return sum(scores) / len(scores)

print("Average [80, 90, 100]:", get_average([80, 90, 100]))
print("Average []:", get_average([]))

# Shallow copy vs real copy
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print("Original:", original, "| Copy:", copy_list)
