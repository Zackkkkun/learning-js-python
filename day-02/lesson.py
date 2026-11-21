"""
DAY 02 LESSON — Types, Precision, Truthiness & Loops (Easy -> Advanced -> Industrial)
Run: python day-02/lesson.py

ANALOGY: Truthiness is a quick yes/no check: empty = False, non-empty = True.
WHEN TO USE:     `for` for known items; `while` for retry/event loops; `Decimal` for money.
WHEN NOT TO USE: Never use `float` for exact financial math, or mutate a list while looping.
JS BRIDGE:       Python `enumerate(arr)` gives `(index, value)` like `arr.forEach((v, i) => ...)`
"""
from decimal import Decimal


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
age = int("25")
print("Next year:", age + 1)

# Core Math & Logic Operators:
#   /  true division (7 / 2 = 3.5)    // floor division (7 // 2 = 3)
#   %  modulo/remainder (7 % 2 = 1)   ** power (2 ** 3 = 8)
#   in / not in  membership check     and / or / not  boolean logic
print("7 // 2 =", 7 // 2, "| 7 % 2 =", 7 % 2, "| 2 ** 3 =", 2 ** 3)

for step in range(1, 6):
    if step == 2:
        continue  # Skip step 2
    if step == 5:
        break     # Stop loop early
    print("Step:", step)

# PREDICT BEFORE RUNNING: What does `bool("")` and `bool("0")` print?
print("bool(''):", bool(""), "| bool('0'):", bool("0"))


# =========================================================
# LEVEL 2: ADVANCED MODE (Precision, Truthiness & Loop Traps)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   short-circuit = Python stops evaluating `or`/`and` as soon as the answer is known

# 1. Float precision trap vs Decimal
print("Float 0.1 + 0.2:", 0.1 + 0.2, "| Decimal:", Decimal("0.1") + Decimal("0.2"))

# 2. Junior vs Senior fallback & filtering
raw_name = ""
# Junior: if raw_name == "": name = "Guest" else: name = raw_name
# Senior:
name = raw_name or "Guest"
print("Fallback:", name)

nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]  # Safe: builds new list instead of mutating!
print("Evens:", evens)

# TRY BREAKING IT (uncomment next line to see ValueError):
# bad = int("3.14")


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: Billing Calculations & Batch API Pagination Loops]

def sum_invoice_cents(prices: list[str]) -> Decimal:
    """Safely sums string prices using Decimal so cents never drift."""
    total = Decimal("0.00")
    for idx, raw in enumerate(prices, start=1):
        total += Decimal(raw)
    return total

print("Invoice total: $", sum_invoice_cents(["19.99", "0.01", "5.50"]))

# FEYNMAN CHECK (answer in 1 sentence):
# -> Why should money calculations use Decimal instead of float?
