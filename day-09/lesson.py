"""
DAY 09 LESSON — Intro to Dictionaries (Phase 2 Kickoff)
Run: python day-09/lesson.py
"""

print("--- DICTIONARIES INTRO ---")
student = {"name": "Zack", "phase": 2, "xp": 1500}

# Access & update
student["xp"] += 100
student["rank"] = "D-Rank"

print("Student:", student)
print("Name:", student["name"])
