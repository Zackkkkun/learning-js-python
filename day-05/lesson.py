"""
DAY 05 LESSON (ADVANCED DEPTH) — Guard Clauses & Mutable Default Trap
Run: python day-05/lesson.py
"""

# =========================================================
# 1. GUARD CLAUSES (FLAT > NESTED)
# =========================================================
print("--- 1. GUARD CLAUSES ---")
def calculate_discount(price: float, member: bool) -> float:
    if price <= 0:
        return 0.0
    if not member:
        return price
    return round(price * 0.85, 2)

print("Member ($100):", calculate_discount(100, True))
print("Edge case (-10):", calculate_discount(-10, True))


# =========================================================
# 2. THE MUTABLE DEFAULT ARGUMENT TRAP
# =========================================================
print("\n--- 2. MUTABLE DEFAULT TRAP ---")
def bad_add(item: str, bag: list[str] = []) -> list[str]:
    bag.append(item)  # BUG: [] is shared across every call!
    return bag

def good_add(item: str, bag: list[str] | None = None) -> list[str]:
    if bag is None:
        bag = []
    bag.append(item)
    return bag

print("Bad call 1:", bad_add("sword"))
print("Bad call 2 (leaked!):", bad_add("potion"))
print("Good call 1:", good_add("sword"))
print("Good call 2 (clean!):", good_add("potion"))
