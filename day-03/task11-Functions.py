"""----------------------------------------------------------
Task 11 — Functions

Functions let you package code so you can reuse it.

def greet(name):
    return f"Hello, {name}!"

print(greet("Sam"))

Write code that:

Defines a function add(a, b) that returns a + b
Calls it with add(5, 3) and prints the result
Defines a second function is_even(n) that returns True if n is even, False otherwise (hint: use n % 2 == 0)
Calls is_even(7) and prints the result

----------------------------------------------------------"""

def add(a, b):
    return a+b

print(add(5,3))

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

# CAN ALSO CODE IT LIKE THIS
#   def is_even(n):
#        return n % 2 == 0

print(is_even(7))