"""
DAY 11 LESSON — Sets (Easy -> Advanced -> Industrial)
Run: python day-11/sets_lesson.py

ANALOGY: A set is a VIP guest list — no duplicates allowed, and the bouncer
         checks if your name is on the list instantly.
WHEN TO USE:     Removing duplicates, fast membership checks (`x in s`), set math.
WHEN NOT TO USE: When order matters, duplicates matter, or you need indexing (`s[0]`).
JS BRIDGE:       Python `set([1, 2, 2])` == JavaScript `new Set([1, 2, 2])`
"""
import time


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
guests = {"Ali", "Sara", "Zack"}
guests.add("Adam")
guests.add("Ali")       # Ignored! Sets never store duplicates
guests.discard("Bob")   # Safe remove (no crash if Bob isn't there)

print("Guest list:", guests)
print("Is Sara invited?", "Sara" in guests)

# Remove duplicates from a list in 1 line:
emails = ["a@x.com", "b@x.com", "a@x.com"]
unique_emails = set(emails)
print("Unique emails:", unique_emails)


# =========================================================
# LEVEL 2: ADVANCED MODE (Under the Hood, Big-O & Traps)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   O(1)      = instant lookup regardless of data size
#   O(n)      = must scan item-by-item (slower as data grows)
#   hashable  = has a fixed fingerprint (immutable: int, str, tuple, frozenset)

# 1. Performance: List scan O(n) vs Set hash-table O(1)
big_list = list(range(200_000))
big_set = set(big_list)
target = 199_999

t0 = time.perf_counter()
_ = target in big_list
t1 = time.perf_counter()
_ = target in big_set
t2 = time.perf_counter()
print(f"List O(n): {(t1 - t0)*1000:.3f} ms | Set O(1): {(t2 - t1)*1000:.4f} ms")

# 2. PREDICT BEFORE RUNNING: What is type({})?
print("PREDICT type({}):", type({}), "| type(set()):", type(set()))

# 3. Junior Way vs Senior Way (Order-preserving deduplication)
tags = ["ai", "python", "ai", "sql"]
# Junior way: loop + `if x not in seen: seen.append(x)`
# Senior way: dict.fromkeys() keeps order AND deduplicates in O(n)!
print("Senior ordered dedupe:", list(dict.fromkeys(tags)))

# 4. Hashability & frozenset (immutable set)
perms = frozenset({"read", "write"})
role_lookup = {perms: "Editor"}
print("frozenset as dict key:", role_lookup[frozenset({"write", "read"})])

# TRY BREAKING IT (uncomment next line to see TypeError: unhashable type):
# bad = {[1, 2]}


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: FastAPI RBAC Auth & RAG Document Chunk Deduplication]

def check_access(user_perms: set[str], required_perms: frozenset[str]) -> tuple[bool, set[str]]:
    """
    Production RBAC (Role-Based Access Control) permission check.
    Returns (is_allowed, missing_permissions).
    """
    missing = required_perms - user_perms
    return (len(missing) == 0, missing)

REQUIRED = frozenset({"read:docs", "write:db"})
user_a = {"read:docs", "write:db", "delete:logs"}
user_b = {"read:docs"}

print("User A access:", check_access(user_a, REQUIRED))
print("User B access:", check_access(user_b, REQUIRED))

# FEYNMAN CHECK (answer in 1 sentence in your head):
# -> Why can a tuple be inside a set, but a list cannot?
