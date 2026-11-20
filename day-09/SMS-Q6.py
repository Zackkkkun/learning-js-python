"""STUDENT MANAGEMENT SYSTEM"""
"""
Q6 — Student Score Validator

Build a program that validates student scores.

Your requirements:
1. Create InvalidScoreError(Exception).
2. Use pass inside the class.
3. Create validate_score(score).
4. Raise InvalidScoreError if score is below 0 or above 100.
5. Return "Valid score" otherwise.
6. Ask the user for a score.
7. Handle ValueError.
8. Catch InvalidScoreError and display its message.
9. Display the returned result for valid scores.
Test cases: 85, 0, 100, -10, 120, hello.

"""

class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if 0 <= score <= 100:
        return "Valid score"
    else:  #BETTER TO REMOVE ELSE BECAUSE ALREADY THE IF ALREADY RETURN MESSAGE
        raise InvalidScoreError("Invalid score!!")

try:
    user_score = float(input("enter your score : "))

    validated_score = validate_score(user_score)
    print(validated_score)

except ValueError:
    print("wth bro input numbers la haiyaa")
    
except InvalidScoreError as e:
    print(e)
