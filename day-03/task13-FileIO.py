"""----------------------------------------------------------
Task 13 — File I/O

Write code that:

Opens a file called notes.txt in write mode
Writes two lines to it: "Learning Python" and "Day 1" (put \n between them for a line break)
Opens the same file again in read mode
Reads and prints its contents

----------------------------------------------------------"""

with open("notes.txt", "w") as f:
    f.write("Learning Python \nDay 1 \nYO SUPPP")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)