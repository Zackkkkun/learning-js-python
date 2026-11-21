"""
DAY 11 LESSON — Sets & Set Operations
Run: python day-11/sets_lesson.py
"""

print("--- 1. UNIQUE ITEMS & DEDUPLICATION ---")
emails = ["a@x.com", "b@x.com", "a@x.com", "c@x.com"]
unique_emails = set(emails)  # Removes duplicates automatically!
print("Unique count:", len(unique_emails), "->", unique_emails)

# Empty set trap:
print("type({}):", type({}), "| type(set()):", type(set()))

print("\n--- 2. SET MATH ---")
py = {"Ali", "Sara", "Zack"}
js = {"Sara", "Zack", "Mika"}
print("Union (|):", py | js)
print("Intersection (&):", py & js)
print("Difference (-):", py - js)  # In py, NOT in js

print("\n--- 3. SAFE REMOVE (.discard vs .remove) ---")
py.discard("Bob")  # Safe: does nothing if missing
try:
    py.remove("Bob")
except KeyError as err:
    print("remove() crashed with KeyError:", err)
