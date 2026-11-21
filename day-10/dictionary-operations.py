"""
Next question — Dictionary operations

Given:

students = {    "Ali": 75,    "Abu": 85,    "Sara": 88,    "Zack": 90}



Write code to:
1. Print all student names using .keys().
2. Print all scores using .values().
3. Remove "Sara" using .pop().
4. Print the number of remaining students using len().
"""

students = {    "Ali": 75,    "Abu": 85,    "Sara": 88,    "Zack": 90}

print(students.keys())
print(students.values())
students.pop("Sara")
print(len(students))
print(students.items()) #output keys and values

"""
Given:
students = {    "Ali": 75,    "Abu": 85,    "Sara": 88}



Write a for loop that prints:
Ali scored 75
Abu scored 85
Sara scored 88


Hint: Use .items(), tuple unpacking, and an f-string.

"""
#students = {    "Ali": 75,    "Abu": 85,    "Sara": 88}
#for student in students.items():
#    print(f"{student.keys()} scored {student.values()}")

students = {    "Ali": 75,    "Abu": 85,    "Sara": 88}
for name, score in students.items():
    print(f"{name} scored {score}")


"""
Start with:
students = {    "Ali": 75,    "Abu": 85,    "Sara": 88,    "Zack": 90}



Your tasks:
1. Add "Mika" with a score of 92.
2. Update "Ali"'s score to 95.
3. Remove "Abu" using .pop().
4. Print all student names using .keys().
5. Print all scores using .values().
6. Use a for loop and .items() to print each student's name and score.
7. Print the total number of students.

"""
students = {    "Ali": 75,    "Abu": 85,    "Sara": 88,    "Zack": 90}

students["Mika"]= 92

students["Ali"]= 95

students.pop("Abu")

print(students.keys())

print(students.values())

for name, score in students.items():
    print(f"{name} scored {score}")

print(len(students))
