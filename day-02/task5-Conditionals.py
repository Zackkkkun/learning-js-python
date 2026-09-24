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
