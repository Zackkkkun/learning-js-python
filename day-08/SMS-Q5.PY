"""STUDENT MANAGEMENT SYSTEM"""

"""
Q5 — Exception Handling
Coding assessment

1. Basic exception handling

Write a program that:
- Asks the user to enter their age.
- Converts the input into an integer.
- Uses try and except to catch ValueError.
- Prints "Invalid age" if the input isn't a valid number.
"""
try:
    age = int(input("enter age : "))
except ValueError:
    print("Invalid age")

"""
2. Multiple exceptions

Write a program that:
- Asks the user to enter two numbers.
- Divides the first number by the second.
- Handles invalid number inputs using ValueError.
- Handles division by zero using ZeroDivisionError.
"""
try:
    num = [int(input("first number : ")), int(input("second number : "))]
    num[0]/num[1]
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot be divided by 0(zero)")


"""
3. Using raise

Write a function called validate_age(age) that:
- Accepts an age.
- Raises a ValueError if the age is below 0.
- Raises a ValueError if the age is above 120.
- Returns "Valid age" if the age is acceptable.
"""
def validate_age(age):
    if age<0:
        raise ValueError("age cannot be below 0")
    elif age>120:
        raise ValueError("age cannot be above 120")
    else:
        return "Valid age"


"""
4. Custom exceptions

Create a custom exception called InsufficientBalanceError.

Then write a function called withdraw(balance, amount) that:
- Raises InsufficientBalanceError if the withdrawal amount exceeds the balance.
- Otherwise, subtracts the amount from the balance.
- Returns the updated balance.
"""
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount>balance:
        raise InsufficientBalanceError("withdrawal amount exceeds the balance")
    else:
        balance = balance - amount
        return balance
    


"""
5. Exception handling with functions

Write a program that:
- Asks the user to enter their bank balance and withdrawal amount.
- Converts both inputs into numbers.
- Uses try/except to handle invalid inputs.
- Calls your withdraw() function from Q4.
- Catches InsufficientBalanceError and displays an appropriate message.
- Displays the updated balance if the withdrawal succeeds.
"""
try: 
    balance = float(input("input balance : "))
    withdrawal_amount = float(input("input withdrawal amount : "))

    updated_balance = withdraw(balance, withdrawal_amount)
    print(updated_balance)
except ValueError:
    print("invalid input")
except InsufficientBalanceError: 
    print("withdrawal amount exceeds the balance")



"""
6. Understanding exceptions through code

Write a small demonstration that:
- Creates a custom exception class inheriting from Exception.
- Uses pass inside the class.
- Raises that exception using raise.
- Catches it using except.
- Displays the exception message.
"""

class ZacksError(Exception):
    pass

def lifes(state):
    if state in ("yes","y"): # ALT if state == "yes" or state == "y":
        print("alhamdulillah brother!")
    if state in ("no", "n"):
        raise ZacksError("WTH IS WRONG WITH YOU?? PUT TRUST IN ALLAH!!")

try:
    life = lifes(input("how's your life? (yes/no) :"))
except ZacksError as e:
    print(e)