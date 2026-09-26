"""----------------------------------------------------------
Task 6 — Loops

Write code that:

Uses a for loop to print numbers 1 to 10
Inside that same loop, skip the number 5 (use continue)
Stop the loop early if the number reaches 8 (use break)

----------------------------------------------------------"""
for i in range(1,11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)


