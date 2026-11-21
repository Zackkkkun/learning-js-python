"""
LESSON — Tuples & Strings in Action
Run this file to see every concept working in real Python code:
    python day-11/tuples_strings_lesson.py
"""

# =========================================================
# 1. TUPLES (Locked lists that cannot be modified)
# =========================================================
print("--- 1. TUPLES ---")
weapon = ("EPIC", {"iron", "dark_crystal"})

# Unpacking: pulls each item into its own variable
rarity, materials = weapon
print("Rarity:", rarity)
print("Materials:", materials)

# 1-item tuple trap:
not_a_tuple = ("ZACK")
real_tuple = ("ZACK",)   # Needs a trailing comma!
print("Without comma:", type(not_a_tuple))  # <class 'str'>
print("With comma:", type(real_tuple))      # <class 'tuple'>

# Immutability: tuples cannot be changed after creation
try:
    real_tuple[0] = "ALI"
except TypeError as err:
    print("Cannot edit a tuple ->", err)


# =========================================================
# 2. STRINGS (Cleaning & splitting text)
# =========================================================
print("\n--- 2. STRINGS ---")
raw = "   LOOT   iron   "

cleaned = raw.strip().lower()  # Removes outer spaces + lowercases
parts = cleaned.split()        # Splits on any spaces -> ["loot", "iron"]
print("Cleaned:", repr(cleaned))
print("Parts:", parts)

# Handling 0, 1, or 2 words safely:
sample = "bag"
words = sample.strip().lower().split()
if len(words) == 0:
    cmd = ("", "")
elif len(words) == 1:
    cmd = (words[0], "")
else:
    cmd = (words[0], words[1])
print("Parsed 'bag' ->", cmd)


# =========================================================
# 3. F-STRINGS & SORTED SETS
# =========================================================
print("\n--- 3. F-STRINGS & SORTED ---")
missing = {"dark_crystal", "iron"}
print(f"Missing: {sorted(missing)}")
print(f"CRAFTED [{rarity}] shadow_blade!")
