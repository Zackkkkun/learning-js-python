"""
Create a dictionary containing these students:

Name	Age	    Score
Ali	    20	    75
Abu	    21	    85
Sara	19	    88

Your program must:
1. Print Ali's score.
2. Change Abu's score to 95.
3. Add Zack, age 22, score 90.
4. Print the updated dictionary.

"""

students = { "ali":{"age":20, "score":75}, "abu":{"age":21, "score":85}, "sara":{"age":19, "score":88}}

students["abu"]["score"]= 95

students["zack"] = {"age":22, "score":90}
print(students)