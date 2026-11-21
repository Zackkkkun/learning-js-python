"""
python_students = {"Ali", "Abu", "Sara", "Zack"}javascript_students = {"Sara", "Zack", "Mika", "John"}



Write code to:
1. Add "Adam" to python_students.
2. Remove "Abu" from python_students.
3. Find all students taking either Python or JavaScript.
4. Find students taking both Python and JavaScript.
5. Print the number of students taking Python.
"""
python_students = {"Ali", "Abu", "Sara", "Zack"}
javascript_students = {"Sara", "Zack", "Mika", "John"}

python_students.add("Adam")

python_students.remove("Abu")

all_students = python_students.union(javascript_students)
print(all_students)

common_students = python_students.intersection(javascript_students)
print(common_students)

print(len(python_students))