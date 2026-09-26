"""----------------------------------------------------------
Task 10 — Sets

Sets are like lists, but they only keep unique values and have no order.

python
a = {1, 2, 3}
b = {3, 4, 5}

Write code that:

Creates those two sets a and b
Prints their union (all values combined) — use a | b
Prints their intersection (values in both) — use a & b
Prints their difference (in a but not b) — use a - b

----------------------------------------------------------"""

a = {1, 2, 3}
b = {3, 4, 5}

print(a|b)
print(a&b)
print(a-b)