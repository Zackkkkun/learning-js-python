"""
DAY 01 LESSON (ADVANCED DEPTH) — Variables, Memory Identity, Lists & Functions
Run: python day-01/lesson.py
"""

# =========================================================
# 1. VARIABLES ARE OBJECT REFERENCES (NOT BOXES)
# =========================================================
print("--- 1. MEMORY & IDENTITY ---")
a = [1, 2, 3]
b = a               # Both point to the SAME list in memory!
b.append(4)
print("a:", a, "| b:", b, "| Same object (a is b):", a is b)

# Use `is None` for None checks, `==` for value equality
x = 1000
y = int("1000")
print("x == y (value):", x == y, "| x is y (memory):", x is y)


# =========================================================
# 2. LISTS UNDER THE HOOD (DYNAMIC ARRAYS)
# =========================================================
print("\n--- 2. LIST COMPLEXITY & COPYING ---")
skills = ["Python", "Git", "AI"]
skills.append("FastAPI")    # O(1) amortized at the end
safe_copy = skills.copy()   # O(n) independent shallow copy
safe_copy.append("Docker")
print("Original:", skills)
print("Copy:", safe_copy)


# =========================================================
# 3. FUNCTIONS & RETURN VALUES
# =========================================================
print("\n--- 3. FUNCTIONS & IMPLICIT NONE ---")
def greet(player: str) -> str:
    return f"Welcome, {player}!"

def no_return() -> None:
    _ = 1 + 1  # Forgot `return` -> returns None automatically

print(greet("Zack"))
print("no_return() ->", no_return())


# =========================================================
# 4. PRODUCTION EDGE CASES
# =========================================================
print("\n--- 4. EDGE CASES ---")
# Dynamic + Strong typing: Python won't silently mix str and int
try:
    _ = "Level " + 4
except TypeError as err:
    print("Strong typing caught:", err)
