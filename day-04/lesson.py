"""
DAY 04 LESSON — Classes (OOP Basics) & Modules
Run: python day-04/lesson.py
"""
import math  # Standard library module

# 1. Classes & Objects
print("--- 1. CLASSES ---")
class Player:
    def __init__(self, name: str, hp: int = 100):
        self.name = name
        self.hp = hp

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)  # Edge case: HP never goes below 0

hero = Player("Zack")
hero.take_damage(35)
print(f"{hero.name} HP after hit:", hero.hp)
hero.take_damage(200)
print(f"{hero.name} HP after overkill:", hero.hp)

# 2. Modules
print("\n--- 2. MODULES ---")
print("Square root of 16:", math.sqrt(16))
