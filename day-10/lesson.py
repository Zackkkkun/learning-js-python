"""
DAY 10 LESSON — Dictionary Operations & Edge Cases
Run: python day-10/lesson.py
"""

print("--- DICTIONARY OPERATIONS ---")
inventory = {"potion": 3, "iron": 5}

# 1. Safe lookup with .get() (no KeyError!)
print("Potions:", inventory.get("potion", 0))
print("Arrows (missing):", inventory.get("arrow", 0))

try:
    _ = inventory["arrow"]
except KeyError as err:
    print("Direct lookup crashed with KeyError:", err)

# 2. Looping over keys and values with .items()
print("\nInventory items:")
for item, qty in inventory.items():
    print(f"  - {item}: {qty}")
