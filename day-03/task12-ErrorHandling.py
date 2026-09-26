"""----------------------------------------------------------
Task 12 — Error Handling (try/except)

Sometimes code crashes — like dividing by zero. try/except lets you catch that instead of crashing the whole program.

python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

Write code that:

Puts 10 / 0 inside a try block
Catches the ZeroDivisionError and prints "Error: division by zero"
Add a finally block that prints "Done" (this runs no matter what)

----------------------------------------------------------"""

try: 
    result = 10/0
except ZeroDivisionError:
    print("Error: division by zero")
finally:
    print("Done")