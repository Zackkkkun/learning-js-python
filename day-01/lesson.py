"""
DAY 01 LESSON — Variables, Lists & Functions (Easy -> Advanced -> Industrial)
Run: python day-01/lesson.py

ANALOGY: A variable is a name tag tied to a balloon (object) in memory.
WHEN TO USE:     Lists for ordered items; functions to reuse logic cleanly.
WHEN NOT TO USE: Don't use `b = a` expecting a separate copy of a list.
JS BRIDGE:       Python `skills.append("AI")` == JS `skills.push("AI")`
"""


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
name = "Zack"
level = 1
skills = ["Python", "Git"]
skills.append("AI")

def greet(player: str) -> str:
    return f"Welcome, {player}!"

print(greet(name), "| Skills:", skills)

# PREDICT BEFORE RUNNING: What does a function without `return` give back?
def silent():
    _ = 1 + 1
print("No return:", silent())


# =========================================================
# LEVEL 2: ADVANCED MODE (Memory References & Big-O)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   reference = pointer to an object's location in RAM
#   amortized = fast on average, even if occasional resize happens

# ASCII Memory Diagram:
#   a ──► [1, 2, 3, 4] ◄── b   (both names point to the SAME list!)
a = [1, 2, 3]
b = a
b.append(4)
print("a:", a, "| b:", b, "| Same object (a is b):", a is b)

# Junior vs Senior copying:
safe_copy = a.copy()  # Independent list!
safe_copy.append(99)
print("Original:", a, "| Safe copy:", safe_copy)

# TRY BREAKING IT (uncomment next line to see Strong Typing TypeError):
# print("Level " + 4)


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: FastAPI Request Validation & AI Agent Tool Output]

def build_user_profile(username: str, tags: list[str] | None = None) -> dict:
    """Builds a clean, normalized user payload for an API response."""
    clean_tags = list(tags) if tags else []
    return {"username": username.strip(), "tags": clean_tags, "active": True}

print("API Payload:", build_user_profile("  zack ", ["python", "ai"]))

# FEYNMAN CHECK (answer in 1 sentence):
# -> Why does changing `b` also change `a` when you write `b = a` on a list?
