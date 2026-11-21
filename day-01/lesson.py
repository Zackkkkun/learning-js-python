"""
DAY 01 LESSON — Hello World, Lists, Functions & Dictionaries
Run: python day-01/lesson.py
"""

# 1. Printing & Variables
print("--- 1. VARIABLES ---")
name = "Zack"
level = 1
print(f"Hello, {name}! Starting at Lv. {level}")

# 2. Lists (ordered, allows duplicates)
print("\n--- 2. LISTS ---")
skills = ["Python", "Git", "AI"]
skills.append("FastAPI")
print("Skills:", skills, "| First:", skills[0], "| Last:", skills[-1])

# 3. Functions (reusable blocks)
print("\n--- 3. FUNCTIONS ---")
def greet(player: str) -> str:
    return f"Welcome, {player}!"

print(greet("Zack"))

# 4. Dictionaries (key -> value)
print("\n--- 4. DICTIONARIES ---")
hero = {"name": "Zack", "rank": "E-Rank"}
print("Hero rank:", hero["rank"])
