#Your Habit Tracker prototype is broken. 
# It should record completed habits, count them, and calculate the completion rate. 
# Your mission is to diagnose and repair the program without rewriting it from scratch.


habits = ["Read", "Exercise", "Code"]
completed = ["Read", "Code", "Code", "Code"]

def count_completed(habits, completed):
    count = 0

    for habit in habits:
        if habit in completed:
#           count =+ 1
            count += 1

    return count

def completion_rate(habits, completed):
    count = count_completed(habits, completed)
    if len(habits) == 0:                                           #added guard clause to prevent division by zero error
        return 0
    return count / len(habits) * 100

print("Completed:", count_completed(habits, completed))
print("Completion rate:", completion_rate(habits, completed), "%")