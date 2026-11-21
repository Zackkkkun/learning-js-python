"""
DAY 05 LESSON — Guard Clauses & Mutable Default Trap (Easy -> Advanced -> Industrial)
Run: python day-05/lesson.py

ANALOGY: Guard clauses are bouncers at the door — reject bad inputs immediately
         at the top so the rest of your function stays clean and flat.
WHEN TO USE:     Early `return`s for validation; `None` as default for list/dict params.
WHEN NOT TO USE: Never put `=[]` or `={}` directly in a `def` parameter!
JS BRIDGE:       JS creates a fresh `[]` default per call; Python reuses the SAME `[]`!
"""


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
def calculate_discount(price: float, member: bool) -> float:
    if price <= 0:
        return 0.0          # Guard 1: invalid price
    if not member:
        return price        # Guard 2: non-member
    return round(price * 0.85, 2)

print("Member ($100):", calculate_discount(100, True))
print("Bad price (-5):", calculate_discount(-5, True))

# Function Parameter Types: positional, keyword, *args, **kwargs
def log_event(event: str, *tags: str, **meta: str) -> None:
    print(f"Event={event} | *tags={tags} | **meta={meta}")

log_event("login", "web", "fast", user="zack", role="dev")


# =========================================================
# LEVEL 2: ADVANCED MODE (The Mutable Default Argument Trap)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   definition time = when Python reads `def ...` once at startup (NOT when called)

# PREDICT BEFORE RUNNING: What does the 2nd call to `bad_add` print?
def bad_add(item: str, bag: list[str] = []) -> list[str]:
    bag.append(item)  # BUG: [] is created ONCE and shared across all calls!
    return bag

print("Bad 1:", bad_add("sword"))
print("Bad 2 (LEAKED!):", bad_add("potion"))

# Senior fix: use `None` + create a fresh list inside
def good_add(item: str, bag: list[str] | None = None) -> list[str]:
    if bag is None:
        bag = []
    bag.append(item)
    return bag

print("Good 1:", good_add("sword"))
print("Good 2 (CLEAN!):", good_add("potion"))


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: API Input Validation & AI Chat History Builders]

def build_chat_messages(user_msg: str, history: list[dict] | None = None) -> list[dict]:
    """Appends a user message to chat history without mutating the caller's list."""
    if not user_msg.strip():
        raise ValueError("Message cannot be empty")
    messages = list(history) if history is not None else []
    messages.append({"role": "user", "content": user_msg.strip()})
    return messages

print("Chat:", build_chat_messages("Hello AI"))

# FEYNMAN CHECK (answer in 1 sentence):
# -> Why is `def f(items=[]):` dangerous in Python?
