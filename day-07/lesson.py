"""
DAY 07 LESSON — LEGB Scope, Closures & Pure Functions (Easy -> Advanced -> Industrial)
Run: python day-07/lesson.py

ANALOGY: LEGB is Python's search ladder: check your pocket (Local) first,
         then backpack (Enclosing), then house (Global), then store (Built-in).
WHEN TO USE:     Pure functions (inputs -> return output) for predictable, testable code.
WHEN NOT TO USE: Avoid mutating `global` variables inside functions.
JS BRIDGE:       Python closures work just like JS functions returning inner functions.
"""


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
xp = 100  # Global

def add_bonus(current_xp: int, bonus: int) -> int:
    return current_xp + bonus

xp = add_bonus(xp, 50)
print("Updated XP:", xp)


# =========================================================
# LEVEL 2: ADVANCED MODE (LEGB, Closures & UnboundLocalError)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   closure = an inner function that "remembers" variables from its outer function

def make_multiplier(factor: int):
    def multiply(value: int) -> int:
        return value * factor  # `factor` comes from Enclosing scope!
    return multiply

double = make_multiplier(2)
print("Closure double(7):", double(7))

# PREDICT BEFORE RUNNING: Why does `count += 1` inside a function crash without `global`?
# Python sees `count = ...` anywhere in the function and marks `count` as LOCAL before running!
# TRY BREAKING IT (uncomment `count += 1` below):
count = 10
def scope_check():
    # count += 1
    return count + 1
print("Read global ok:", scope_check())


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: FastAPI Dependency Factories & Rate Limiters]

def make_rate_checker(max_requests: int):
    """Creates a reusable validator configured with a fixed limit."""
    def is_allowed(current_count: int) -> bool:
        return current_count < max_requests
    return is_allowed

free_tier_ok = make_rate_checker(10)
print("Free tier (req #5):", free_tier_ok(5), "| (req #10):", free_tier_ok(10))

# FEYNMAN CHECK (answer in 1 sentence):
# -> What do the 4 letters in LEGB stand for?
