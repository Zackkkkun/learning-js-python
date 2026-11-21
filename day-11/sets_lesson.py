"""
DAY 11 LESSON (ADVANCED DEPTH) — Sets, Hashing & Performance
Run: python day-11/sets_lesson.py
"""
import time

# =========================================================
# 1. UNDER THE HOOD: HASH TABLES & O(1) LOOKUP
# =========================================================
print("--- 1. PERFORMANCE: SET vs LIST ---")
big_list = list(range(200_000))
big_set = set(big_list)
target = 199_999

t0 = time.perf_counter()
_ = target in big_list  # O(n): scans item by item
t1 = time.perf_counter()
_ = target in big_set   # O(1): jumps straight via hash!
t2 = time.perf_counter()

print(f"List lookup: {(t1 - t0)*1000:.3f} ms | Set lookup: {(t2 - t1)*1000:.4f} ms")


# =========================================================
# 2. HASHABILITY RULE & FROZENSET
# =========================================================
print("\n--- 2. HASHABILITY & FROZENSET ---")
# Sets can ONLY hold immutable (hashable) items: int, str, tuple.
valid_set = {(1, 2), "ok", 42}
print("Set with tuple:", valid_set)

try:
    bad_set = {[1, 2]}  # Lists are mutable -> unhashable!
except TypeError as err:
    print("List inside set crashed:", err)

# frozenset: an immutable set (can be used inside another set or as a dict key!)
perms_key = frozenset({"read", "write"})
role_map = {perms_key: "Editor"}
print("frozenset as dict key:", role_map[frozenset({"write", "read"})])


# =========================================================
# 3. FULL SET ALGEBRA & SUBSET CHECKS
# =========================================================
print("\n--- 3. SET ALGEBRA & SUBSETS ---")
required = {"python", "sql"}
candidate_a = {"python", "sql", "fastapi", "docker"}
candidate_b = {"python", "react"}

print("A meets all requirements (issuperset):", candidate_a >= required)
print("Required subset of B:", required <= candidate_b)
print("Union (|):", candidate_a | candidate_b)
print("Intersection (&):", candidate_a & candidate_b)
print("Difference (-):", candidate_a - candidate_b)
print("Symmetric Diff (^, in one OR other, not both):", candidate_a ^ candidate_b)


# =========================================================
# 4. PRODUCTION EDGE CASES
# =========================================================
print("\n--- 4. EDGE CASES ---")
# Trap 1: {} is an empty DICT, not an empty set!
print("type({}):", type({}), "| type(set()):", type(set()))

# Trap 2: Order-preserving deduplication (dict.fromkeys vs set)
tags = ["ai", "python", "ai", "sql", "python"]
print("set() loses order:", list(set(tags)))
print("dict.fromkeys() keeps order:", list(dict.fromkeys(tags)))

# Trap 3: remove() vs discard()
s = {"a", "b"}
s.discard("missing")  # Safe no-op
try:
    s.remove("missing")
except KeyError as err:
    print("remove() raised KeyError:", err)
