"""STUDENT MANAGEMENT SYSTEM"""

"""
Q1 — List Basics

Create a Python list containing at least 3 student names.

Your program must:
1. Display the second student's name.
2. Change the first student's name to "Zack".
3. Add one new student to the end.
4. Display the updated list.
5. Display the total number of students using len().

"""

stud_name=["A","B","C"]
print(stud_name[1])
stud_name[0]="Zack"
stud_name.append("D")
print(stud_name)
print(len(stud_name))
