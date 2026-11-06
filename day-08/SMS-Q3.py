"""STUDENT MANAGEMENT SYSTEM"""

"""
Q3 — Functions & Return

Now let's test whether you can make functions work together.

Create two functions:

Function 1: calculate_average(scores)
- Accept a list of scores.
- Calculate the average.
- Return the average.
Function 2: get_grade(average)
- Accept the average.
- Return a grade based on these rules:
Average	Grade
80–100	A
70–79	B
60–69	C
50–59	D
Below 50	F

Then:
1. Create a list: [85, 70, 90, 65].
2. Pass it into calculate_average().
3. Pass the returned average into get_grade().
4. Print the average and grade.
"""

#not the best approach. can be simplified
def calculate_average(scores):

    i = 0
    average = 0
    while i in range(0, len(scores)):
        average += scores[i]
        i += 1
    average = average/len(scores)
    return average



"""
WRONG BECAUSE RANGE() READS INTEGER ONLY. 77.5 IS NOT INTEGER THEN IT PASSES TO ELSE CONDITION.
def get_grade(average):

    if average in range(80, 101):
        grade = "A"
        return grade

    elif average in range(70, 80):
        grade = "B"
        return grade

    elif average in range(60, 70):
        grade = "C"
        return grade

    elif average in range(50, 60):
        grade = "D"
        return grade

    elif average in range(0, 50):
        grade = "F"
        return grade

    else:
        grade = "Grade out of range"

    return grade
"""

def get_grade(average):

    if 80 <= average <= 100:
        grade = "A"
        return grade

    elif 70 <= average < 80:
        grade = "B"
        return grade

    elif 60 <= average < 70:
        grade = "C"
        return grade

    elif 50 <= average < 60:
        grade = "D"
        return grade

    elif 0 <= average < 50:
        grade = "F"
        return grade

    else:
        grade = "Grade out of range"

    return grade


student_scores = [85, 70, 90, 65]
avg_score = calculate_average(student_scores)
avg_grade = get_grade(avg_score)
print(avg_score)
print(avg_grade)


"""
ALTERNATIVES
----------------------------------------------------------------------------------------------------------------------------------------------
|| 1. calculate_average(scores) ||

The objective is to accept a list, calculate its average and return the result.

Method A — while loop (your approach)
>
def calculate_average(scores):
    i = 0
    total = 0

    while i < len(scores):
        total += scores[i]
        i += 1

    average = total / len(scores)
    return average

# Concepts: indexing, while, accumulator, len().


Method B — for loop
>
def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)

# Concepts: iteration directly over list elements.


Method C — sum()
>
def calculate_average(scores):
    return sum(scores) / len(scores)

# sum() is a built-in Python function that adds all numerical elements in an iterable.


Method D — List comprehension
>
def calculate_average(scores):
    total = sum([score for score in scores])
    return total / len(scores)

# This works, but it adds unnecessary complexity here. List comprehension is more useful when transforming or filtering collections.

Method E — statistics.mean()
>
import statistics
def calculate_average(scores):
    return statistics.mean(scores)

# Python's standard library already provides a function for arithmetic means.

+--------------Comparison--------------------------------------------+
Method	|    Main technique	      |      Practical use
----------------------------------------------------------------------
A	    |    while	              |      Learning loops and indexing
B	    |    for	General       |      iteration
C	    |    sum()	              |      Concise everyday Python
D	    |    Comprehension	      |      Transforming collections
E	    |    statistics.mean()	  |      Statistical calculations


--------------------------------------------------------------------------------------------------------------------------------------------

||2. get_grade(average)||

The objective is to return a grade based on numerical boundaries.

Method A — if / elif with range() (your original approach)
>
def get_grade(average):
    if average in range(80, 101):
        return "A"
    elif average in range(70, 80):
        return "B"
    elif average in range(60, 70):
        return "C"
    elif average in range(50, 60):
        return "D"
    else:
        return "F"

# Limitation: range() produces integers, so it doesn't work correctly for decimal averages.


Method B — Comparison operators (your corrected approach)
>
def get_grade(average):
    if 80 <= average <= 100:
        return "A"
    elif 70 <= average < 80:
        return "B"
    elif 60 <= average < 70:
        return "C"
    elif 50 <= average < 60:
        return "D"
    elif 0 <= average < 50:
        return "F"
    else:
        return "Grade out of range"

# This supports decimals and makes the boundaries explicit.


Method C — Comparison operators with simpler conditions
>
def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 0:
        return "F"
    else:
        return "Grade out of range"

# Why does this work?
# Python checks conditions from top to bottom. Once a condition is true, it returns the corresponding grade.
# For example, if average is 77.5:
# - 77.5 >= 80 → False
# - 77.5 >= 70 → True
# - Return "B".
# This is a common and readable approach when the conditions are ordered.


Method D — Dictionary lookup (not suitable for continuous averages)
>
grades = {
    80: "A",
    70: "B",
    60: "C",
    50: "D",
    0: "F"
}

# A dictionary directly maps keys to values. However, you would need additional logic to find which threshold applies.
# A plain dictionary lookup cannot automatically determine numerical ranges.


Method E — match/case (Python 3.10+)
>
def get_grade(average):
    match average:
        case x if x >= 80:
            return "A"
        case x if x >= 70:
            return "B"
        case x if x >= 60:
            return "C"
        case x if x >= 50:
            return "D"
        case x if x >= 0:
            return "F"
        case _:
            return "Grade out of range"

# This is possible, but if/elif is simpler for this particular task.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
||3. Putting everything together||

You can combine different approaches without changing the overall program structure.

Version 1 — Beginner-friendly
# Good for learning fundamentals
>
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 0:
        return "F"
    return "Grade out of range"

student_scores = [85, 70, 90, 65]

avg_score = calculate_average(student_scores)
avg_grade = get_grade(avg_score)

print(avg_score)
print(avg_grade)

---

Version 2 — Python concise style
import statistics

def calculate_average(scores):
    return statistics.mean(scores)

def get_grade(average):
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    if average >= 0:
        return "F"
    return "Grade out of range"

student_scores = [85, 70, 90, 65]

avg_score = calculate_average(student_scores)
avg_grade = get_grade(avg_score)

print(avg_score)
print(avg_grade)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. What about real-world code?

There are additional considerations beyond the exercise:
----------------------------------------------------------------|
Situation	         |   What should be handled?                |
----------------------------------------------------------------|
Empty score list	 |   Avoid division by zero                 |
Negative score	     |   Reject invalid score                   |
Score above 100	     |   Reject invalid score                   |
Non-numeric input	 |   Handle ValueError                      |
Decimal scores	     |   Support floating-point numbers         |
Large datasets	     |   Consider performance and data handling |

For example, calculate_average([]) would cause a ZeroDivisionError in your original approach. 
A production implementation should define what happens when the list is empty.

5. My recommendation for your learning

Don't just memorize the shortest version.

Understand these in order:
--1. while loop + indexing.
--2. for loop + accumulator.
--3. sum() + len().
--4. Comparison operators for numerical ranges.
--5. Functions communicating through return.
These are transferable skills you'll use in larger systems.

One important distinction: There isn't one universally best coding style. 
The best approach depends on readability, maintainability, performance and the problem being solved.
"""