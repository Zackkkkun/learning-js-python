"""
DAY 02 LESSON — Types, Conversion, Strings, Operators, Conditionals & Loops
Run: python day-02/lesson.py
"""

# 1. Types & Conversion
print("--- 1. TYPE CONVERSION ---")
raw_age = "25"
age = int(raw_age)
print("25 + 5 =", age + 5)

try:
    bad = int("abc")
except ValueError as err:
    print("Edge case (bad int):", err)

# 2. Operators & Conditionals
print("\n--- 2. CONDITIONALS ---")
score = 85
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(f"Score {score} -> Grade {grade}")

# 3. Loops (for & while)
print("\n--- 3. LOOPS ---")
for i in range(1, 4):
    print("for step:", i)

count = 3
while count > 0:
    print("while countdown:", count)
    count -= 1  # Always update exit condition!
