"""
DAY 08 LESSON — Safe Aggregation & Shallow vs Deep Copy (Easy -> Advanced -> Industrial)
Run: python day-08/lesson.py

ANALOGY: Shallow copy duplicates the folder, not the files inside;
         Deep copy duplicates the folder AND every nested file inside it.
WHEN TO USE:     `copy.deepcopy()` when copying nested lists/dicts (like JSON payloads).
WHEN NOT TO USE: Don't use `.copy()` on nested structures if you'll edit inner items!
JS BRIDGE:       Python `copy.deepcopy(obj)` == JS `structuredClone(obj)`
"""
import copy


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
def get_average(scores: list[int]) -> float:
    if not scores:
        return 0.0  # Empty list guard!
    return sum(scores) / len(scores)

print("Average:", get_average([80, 90, 100]), "| Empty:", get_average([]))


# =========================================================
# LEVEL 2: ADVANCED MODE (Shallow vs Deep Copy Trap)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# ASCII Memory Diagram:
#   team    ──► [ ptr1 ──► ["Zack", 100], ptr2 ──► ["Sara", 95] ]
#   shallow ──► [ ptr1 (SAME inner list!), ptr2 ]

team = [["Zack", 100], ["Sara", 95]]
shallow = team.copy()
shallow[0][1] = 0
print("PREDICT team after shallow edit:", team)  # Zack's score changed in BOTH!

team = [["Zack", 100], ["Sara", 95]]
deep = copy.deepcopy(team)
deep[0][1] = 0
print("team after deep edit:", team, "| deep:", deep)


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: Cloning Config Templates & LLM Request Payloads]

BASE_LLM_CONFIG = {"model": "gemini-flash", "params": {"temperature": 0.2}}

def make_creative_config() -> dict:
    """Deep-copies base config so changing temperature never mutates the global template."""
    cfg = copy.deepcopy(BASE_LLM_CONFIG)
    cfg["params"]["temperature"] = 0.9
    return cfg

print("Creative:", make_creative_config(), "| Base untouched:", BASE_LLM_CONFIG)

# FEYNMAN CHECK (answer in 1 sentence):
# -> When is `list.copy()` NOT enough to protect original data?
