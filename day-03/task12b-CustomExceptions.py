"""----------------------------------------------------------
Task 12b — Custom Exceptions

Write code that:

Creates a custom exception class called TooYoungError (inherits from Exception)
Writes a function check_age(age) that raises TooYoungError("Must be 18+") if age < 18
Wraps a call like check_age(15) in a try/except and prints the error message when caught

Reminder of the pattern from earlier:

python
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number can't be negative!")
    return n

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Caught custom error:", e)

----------------------------------------------------------"""

class TooYoungError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise TooYoungError("Must be 18+")
    return age

try:
    check_age(15)
except TooYoungError as e:
    print("Error occured:", e)