"""
DAY 11 LESSON (ADVANCED DEPTH) — Tuples, Unpacking, Strings & Memory
Run: python day-11/tuples_strings_lesson.py
"""

# =========================================================
# 1. TUPLES: STAR UNPACKING & MUTABLE-INSIDE-IMMUTABLE TRAP
# =========================================================
print("--- 1. ADVANCED TUPLES ---")
record = ("Zack", "D-Rank", 100, 150, 200)
name, rank, *scores = record  # Star unpacking grabs remaining items as a list
print(f"Name: {name}, Rank: {rank}, Scores: {scores}")

# Swap variables in 1 line without a temp variable (uses tuple packing/unpacking)
a, b = 10, 99
a, b = b, a
print("Swapped:", a, b)

# 1-item tuple trap:
print("type(('ZACK')):", type(("ZACK")), "| type(('ZACK',)):", type(("ZACK",)))

# Subtle trap: a tuple locks REFERENCES, not mutable objects inside it!
tricky = ("locked_str", [1, 2])
tricky[1].append(3)  # Allowed! The list itself mutated, though the tuple slot didn't
print("Mutable list inside tuple:", tricky)


# =========================================================
# 2. STRINGS: SPLIT EDGE CASES & PERFORMANCE
# =========================================================
print("\n--- 2. STRING PARSING & EDGE CASES ---")
# Trap: .split() vs .split(",") on empty/whitespace strings!
print("''.split() ->", "".split())          # []
print("''.split(',') ->", "".split(","))    # ['']  <-- Watch out!

# .partition() always returns a clean 3-tuple: (before, sep, after)
header = "Authorization: Bearer tok_123"
key, _, val = header.partition(": ")
print(f"Key={key!r}, Val={val!r}")

# .startswith() accepts a TUPLE of prefixes (cleaner than multiple `or`s!)
filename = "report_2026.csv"
print("Is data file:", filename.endswith((".csv", ".json", ".parquet")))

# Performance: Building big strings with "".join(parts) is O(n),
# whereas += inside a large loop creates new string copies every time!
words = ["  Python ", " FASTAPI", " ai "]
cleaned = " | ".join(w.strip().lower() for w in words)
print("Joined:", cleaned)


# =========================================================
# 3. F-STRING FORMATTING SPECIFIERS
# =========================================================
print("\n--- 3. F-STRING SPECIFIERS ---")
pi = 3.1415926
xp = 1600
print(f"Rounded: {pi:.2f} | Comma-formatted: {xp:,} | Padded: [{name:>8}]")
