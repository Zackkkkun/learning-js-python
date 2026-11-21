"""
DAY 04 LESSON — Classes, Dataclasses & Modules (Easy -> Advanced -> Industrial)
Run: python day-04/lesson.py

ANALOGY: A class is a blueprint; objects are houses built from that blueprint.
WHEN TO USE:     Classes/dataclasses to bundle related data + behavior cleanly.
WHEN NOT TO USE: Don't force a class when a simple function or dict is clearer.
JS BRIDGE:       Python `__init__(self)` == JS `constructor()` (`self` == `this`)
"""
from dataclasses import dataclass


# =========================================================
# LEVEL 1: EASY MODE (The Intuition — 30 Seconds)
# =========================================================
print("=== LEVEL 1: EASY MODE ===")
class Player:
    def __init__(self, name: str, hp: int = 100):
        self.name = name
        self.hp = hp

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

hero = Player("Zack")
hero.take_damage(35)
print(f"{hero.name} HP:", hero.hp)

# PREDICT BEFORE RUNNING: What is `__name__` when you run this file directly?
print("PREDICT __name__:", __name__)


# =========================================================
# LEVEL 2: ADVANCED MODE (__repr__ & Frozen Dataclasses)
# =========================================================
print("\n=== LEVEL 2: ADVANCED MODE ===")
# GLOSSARY:
#   dunder method = "double underscore" special method like __init__, __repr__
#   frozen        = immutable dataclass (cannot modify fields after creation)

# Junior: writing __init__, __repr__, __eq__ manually for data-only classes
# Senior: @dataclass writes them for you automatically!
@dataclass(frozen=True)
class Quest:
    title: str
    xp: int

q = Quest("Engine v0.1", 150)
print("Dataclass:", q)

# TRY BREAKING IT (uncomment next line to see FrozenInstanceError):
# q.xp = 999


# =========================================================
# LEVEL 3: INDUSTRIAL MODE (Real Backend & AI Production)
# =========================================================
print("\n=== LEVEL 3: INDUSTRIAL MODE ===")
# [USED IN: FastAPI Schemas & LLM Structured Output Models]

@dataclass(frozen=True)
class LLMResponse:
    model: str
    answer: str
    tokens_used: int

    def is_within_budget(self, max_tokens: int) -> bool:
        return self.tokens_used <= max_tokens

resp = LLMResponse(model="gemini-flash", answer="Use a set.", tokens_used=42)
print("Response:", resp, "| Under budget:", resp.is_within_budget(100))

# FEYNMAN CHECK (answer in 1 sentence):
# -> What does `if __name__ == "__main__":` protect against when a file is imported?
