"""----------------------------------------------------------
Task 5 — Conditionals

Write code that:

Creates a variable score = 72
Prints "Pass" if score >= 50, otherwise prints "Fail"
Then extend it: print "A" if score >= 90, "B" if score >= 75, "C" if score >= 50, else "F"

----------------------------------------------------------"""

score = 72

if score >= 50:
    print("Pass")
else:
    print("Fail")

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")

"""
Alternative 1: Nested if/else (older style, does the same thing as elif but more indentation)

python
if score >= 90:
    print("A")
else:
    if score >= 75:
        print("B")
    else:
        if score >= 50:
            print("C")
        else:
            print("F")

"""

"""
Alternative 2: Using a function that returns the grade

python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

print(get_grade(72))
            
"""