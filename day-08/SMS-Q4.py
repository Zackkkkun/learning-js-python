"""STUDENT MANAGEMENT SYSTEM"""

"""
1. Global variable

Create a global variable balance = 500.

Write a function show_balance() that prints the balance.

"""


balance = 500

def show_balance():
 #  global balance     #not needed because we are only reading balance. not modifying it
    print(balance)

show_balance()




"""
2. Local variable

Write a function temporary_balance() that creates a local variable named balance = 1000 and prints it. Then print the global balance outside the function.

"""
balance = 500

def temporary_balance():
    balance = 1000
    print(balance)

temporary_balance()
print(balance)


"""
3. Global keyword

Write a function update_total() that adds 50 to the global variable total = 100 using global.
"""
total = 100
def update_total():
    global total
    total += 50

update_total()
print(total)

"""
4. Parameters & return

Write a function deposit(current_balance, amount) that:
- Adds the amount to the current balance.
- Returns the new balance.
- Updates the original balance using the returned value.
Test with RM500 + RM100.
"""
balance = 500

def deposit(current_balance, amount):
    current_balance += amount
    return current_balance

balance = deposit(balance, 100)
print(balance)

"""
5. Withdrawal

Write a function withdraw(current_balance, amount) that:
- Subtracts the amount from the current balance.
- Returns the new balance.
- Does not use global.
Test with RM500 - RM100.
"""
balance = 500
def withdraw(current_balance, amount):
    current_balance -= amount
    return current_balance

balance = withdraw(balance, 100)
print(balance)