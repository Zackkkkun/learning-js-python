"""
DAY 07 LESSON (ADVANCED DEPTH) — LEGB Scope, Closures & Composition
Run: python day-07/lesson.py
"""

# =========================================================
# 1. LEGB SCOPE RESOLUTION (LOCAL -> ENCLOSING -> GLOBAL -> BUILTIN)
# =========================================================
print("--- 1. LEGB SCOPE ---")
xp = 100  # Global

def make_multiplier(factor: int):
    # Enclosing scope: `factor` is remembered by the inner function (closure)!
    def multiply(value: int) -> int:
        return value * factor  # Local + Enclosing
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print("double(5):", double(5), "| triple(5):", triple(5))


# =========================================================
# 2. PURE FUNCTIONS & COMPOSITION
# =========================================================
print("\n--- 2. PURE FUNCTION COMPOSITION ---")
def add_bonus(current_xp: int, bonus: int) -> int:
    return current_xp + bonus  # Pure: doesn't mutate outer `xp`

new_xp = add_bonus(double(50), 25)
print("Composed result:", new_xp, "| Outer xp untouched:", xp)


# =========================================================
# 3. EDGE CASE: UNBOUNDLOCALERROR
# =========================================================
print("\n--- 3. UNBOUNDLOCALERROR TRAP ---")
count = 10
def broken():
    # Assigning to `count` anywhere in the function makes Python treat it as local!
    return count + 1  # Reading is fine; `count += 1` without `global` crashes!

print("Reading global is ok:", broken())
