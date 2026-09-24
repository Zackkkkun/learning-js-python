"""----------------------------------------------------------
Task 2 — Type Conversion

Write code that:

Creates price_str = "19.99" (a string)
Converts it to a float and stores it in a new variable
Adds 5.01 to that float
Prints the result as: Total: 25.0
----------------------------------------------------------"""
price_str = "19.99"
price_float = float(price_str)
total = price_float + 5.01

print(f"Total : {total}")
