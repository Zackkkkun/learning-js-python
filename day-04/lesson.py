"""
DAY 04 LESSON (ADVANCED DEPTH) — Classes, Dunder Methods & Modules
Run: python day-04/lesson.py
"""
from dataclasses import dataclass

# =========================================================
# 1. CLASSES, ENCAPSULATION & __repr__
# =========================================================
print("--- 1. CLASSES & DUNDER METHODS ---")
class Player:
    def __init__(self, name: str, hp: int = 100):
        self.name = name
        self.hp = hp

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        self.hp = max(0, self.hp - amount)

    def __repr__(self) -> str:
        return f"Player(name={self.name!r}, hp={self.hp})"

hero = Player("Zack")
hero.take_damage(35)
print("Repr:", hero)


# =========================================================
# 2. DATACLASSES (MODERN PYTHON DATA MODELS)
# =========================================================
print("\n--- 2. DATACLASSES ---")
@dataclass(frozen=True)  # frozen=True makes it immutable & hashable!
class Quest:
    title: str
    xp: int

q = Quest("Build Engine", 150)
print("Immutable Quest:", q)


# =========================================================
# 3. MODULE GUARD (__name__ == "__main__")
# =========================================================
print("\n--- 3. MODULE NAME ---")
print("Current __name__:", __name__)  # "__main__" when run directly, module name when imported
