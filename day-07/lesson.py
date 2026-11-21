"""
DAY 07 LESSON — Variable Scope (Local vs Global) & Function Composition
Run: python day-07/lesson.py
"""

# 1. Local vs Global Scope
print("--- 1. VARIABLE SCOPE ---")
xp = 100  # Global

def add_bonus(current_xp: int, bonus: int) -> int:
    # Prefer returning a new value instead of mutating globals!
    new_xp = current_xp + bonus
    return new_xp

xp = add_bonus(xp, 50)
print("Updated XP:", xp)

# 2. Function Composition (output of one feeds the next)
print("\n--- 2. FUNCTION COMPOSITION ---")
def double(x: int) -> int:
    return x * 2

def add_ten(x: int) -> int:
    return x + 10

result = add_ten(double(5))  # double(5)=10 -> add_ten(10)=20
print("add_ten(double(5)) =", result)
