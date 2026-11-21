"""
DAY 02 LESSON (ADVANCED DEPTH) — Types, Precision, Truthiness & Loops
Run: python day-02/lesson.py
"""
from decimal import Decimal

# =========================================================
# 1. TYPE CONVERSION & FLOAT PRECISION
# =========================================================
print("--- 1. TYPE CONVERSION & FLOAT TRAP ---")
print("0.1 + 0.2 in float:", 0.1 + 0.2)  # Binary float rounding!
print("Exact Decimal:", Decimal("0.1") + Decimal("0.2"))

try:
    _ = int("3.14")  # Crashes even though it looks numeric!
except ValueError as err:
    print("int('3.14') crashed:", err)


# =========================================================
# 2. TRUTHINESS & SHORT-CIRCUIT LOGIC
# =========================================================
print("\n--- 2. TRUTHINESS & FALLBACKS ---")
# Falsy values: False, None, 0, "", [], {}, set(), ()
raw_name = ""
display_name = raw_name or "Guest"  # Short-circuits to "Guest"
print("Fallback name:", display_name)


# =========================================================
# 3. PYTHONIC LOOPS (ENUMERATE & MUTATION TRAP)
# =========================================================
print("\n--- 3. LOOPS & MUTATION TRAP ---")
items = ["a", "b", "c"]
for idx, val in enumerate(items, start=1):
    print(f"  {idx}. {val}")

# Never remove from a list while looping over it! Build a new list instead:
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print("Filtered evens:", evens)
