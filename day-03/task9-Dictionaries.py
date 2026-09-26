"""----------------------------------------------------------
Task 9 — Dictionaries

Write code that:

Creates a dictionary person = {"name": "Alex", "age": 25}
Prints the value for "name" — use person["name"]
Adds a new key "city" with value "KL" — use person["city"] = "KL"
Updates "age" to 26 — same syntax as adding, just an existing key
Prints the whole dictionary

----------------------------------------------------------"""

person = {"name":"Alex", "age":25}
print(person["name"])
person["city"] = "KL"
person["age"] = 26
print(person)