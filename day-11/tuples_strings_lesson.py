"""
DAY 11 LESSON — Tuples & Strings (Easy -> Advanced -> Industrial)
Run: python day-11/tuples_strings_lesson.py

ANALOGY: A tuple is a sealed envelope (fixed order, locked contents).
         A string is an immutable row of characters — every edit makes a new copy.
WHEN TO USE:     Tuples for fixed records & multi-value returns; strings for text.
WHEN NOT TO USE: Tuples when you need to add/remove items later (use a list).
JS BRIDGE:       Python `tuple` ~ JS `Object.freeze([...])`; `f"{x}"` == JS `` `${x}` ``
"""


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
# Tuple packing & unpacking
weapon = ("Shadow Blade", "EPIC", 45)
name, rarity, power = weapon
print(f"Item: {name} | Rarity: {rarity} | Power: {power}")

# String cleaning pipeline (each method explained!)
raw = "   LOOT  iron   "
print("1. .strip() ->", repr(raw.strip()))            # Removes spaces on BOTH ends
print("2. .lstrip() ->", repr(raw.lstrip()))          # Left spaces only
print("3. .rstrip() ->", repr(raw.rstrip()))          # Right spaces only
print("4. .lower() ->", repr(raw.strip().lower()))    # All lowercase
print("5. .upper() ->", repr(raw.strip().upper()))    # ALL UPPERCASE
print("6. .title() ->", repr("zack kun".title()))     # "Zack Kun"
print("7. .split() ->", raw.strip().lower().split())  # Splits into list of words
print("8. .replace() ->", "hi_ai".replace("_", " "))  # Replaces text
print("9. .find() ->", "hello".find("e"), "| missing:", "hello".find("z"))  # Index or -1
print("10. .isdigit() ->", "123".isdigit(), "| .isalpha() ->", "abc".isalpha())
print("11. slicing [::-1] ->", "python"[::-1])        # Reverses string: "nohtyp"
print("12. tuple .count()/.index() ->", (1, 2, 2).count(2), (10, 20, 30).index(20))

# PREDICT BEFORE RUNNING: What type is ("ZACK") vs ("ZACK",)?
print("No comma:", type(("ZACK")), "| With comma:", type(("ZACK",)))


# =========================================================
# LEVEL 2: ADVANCED MODE (Under the Hood, Memory & Traps)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   immutable = cannot be modified in memory after creation
#   O(n²)     = gets quadratically slower as input grows (avoid `+=` in big loops!)

# 1. Star unpacking & 1-line variable swap
record = ("Zack", "D-Rank", 100, 150, 200)
player, rank, *scores = record
print(f"Player={player}, Rank={rank}, Scores={scores}")

a, b = 10, 99
a, b = b, a  # Uses tuple packing/unpacking under the hood
print("Swapped:", a, b)

# 2. ASCII Memory Trap: Tuple locks REFERENCES, not mutable objects inside!
#   tricky ──► ( "locked_str" ,  ptr ──► [1, 2] )
#                                         ▲ can still .append(3)!
tricky = ("locked_str", [1, 2])
tricky[1].append(3)
print("Mutable list inside tuple:", tricky)

# 3. Junior Way vs Senior Way (Building strings & splitting)
words = ["  Python ", " FASTAPI", " ai "]
# Junior: loop with `result += w + " | "`  (O(n²) string copying!)
# Senior: generator + " | ".join(...)     (O(n) single allocation!)
print("Senior join:", " | ".join(w.strip().lower() for w in words))

# 4. Split edge case:
print("''.split() ->", "".split(), "| ''.split(',') ->", "".split(","))

# TRY BREAKING IT (uncomment next line to see TypeError):
# weapon[0] = "New Name"


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: HTTP Header Parsing & LLM Prompt/Command Sanitization]

def parse_auth_header(header: str) -> tuple[str, str]:
    """
    Safely splits an HTTP header like 'Authorization: Bearer tok_123'.
    Uses .partition() so colons inside the value never break parsing.
    """
    key, sep, val = header.partition(": ")
    if not sep:
        return ("", "")
    return (key.strip().lower(), val.strip())

print("Parsed header:", parse_auth_header("Authorization: Bearer tok_123"))
print("Bad header:", parse_auth_header("invalid_header"))

# FEYNMAN CHECK (answer in 1 sentence in your head):
# -> Why is "".join(parts) faster than using += inside a large loop?
