"""STUDENT MANAGEMENT SYSTEM"""

"""
Q2 — Removing Students

---
Start with this list:
students = ["Ali", "Abu", "Amin", "Sara", "Mira"]
---

Your tasks:
1. Remove "Abu" using .remove().
2. Remove the last student using .pop().
3. Store the removed student in a variable called removed_student.
4. Print removed_student.
5. Print the updated list.
6. Print the total number of remaining students.

"""

students = ["Ali", "Abu", "Amin", "Sara", "Mira"]
students.remove("Abu")
removed_student = students.pop()
print(removed_student)
print(students)
print(len(students))