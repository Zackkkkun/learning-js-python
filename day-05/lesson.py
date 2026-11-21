"""
DAY 05 LESSON — Functions & Guard Clauses (Mission Foundations)
Run: python day-05/lesson.py
"""

# Guard clauses handle edge cases early so code stays flat and readable
print("--- GUARD CLAUSES ---")
def calculate_discount(price: float, member: bool) -> float:
    if price <= 0:
        return 0.0
    if not member:
        return price
    return round(price * 0.85, 2)

print("Member ($100):", calculate_discount(100, True))
print("Guest ($100):", calculate_discount(100, False))
print("Edge case (-10):", calculate_discount(-10, True))
