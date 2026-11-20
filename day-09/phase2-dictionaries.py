"""DICTIONARIES"""

"""
Q1 — Student Records
Create a dictionary named students containing three students and their scores.

Requirements:
1. Store three student names as keys.
2. Store their scores as values.
3. Print the score of the second student.
4. Change the first student's score.
5. Add a fourth student.
6. Print the complete dictionary.

"""

students = {
    "alif": 23, "amar": 99, "ikram": 76
}

print(students["amar"])
students["amar"]= 100
students["aryan"]= 85
print(students)