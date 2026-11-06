'''import random

num = random.randint(1,10)
guess = -9999999

while guess != num:
    guess = int(input("guess a number [1-10] "))

    if guess == num:
        print("correct!!")
    else:
        print("YOU WRONG MF!!")


# rejecting guess outside 1-10 range
import random

num = random.randint(1,10)
guess = -9999999

while guess != num:
    guess = int(input("guess a number [1-10] "))

    if guess in range(1,11):                    #can also write like this    # if 1 <= guess <= 10: #      
        if guess == num:
            print("correct!!")
        elif guess > num:
            print("too high")
        else:
            print("too low")
    else:
        print("range must be within 1-10")


'''
#solving wrong value input problem (try-except)
import random

num = random.randint(1,10)
guess = -9999999

while guess != num:
    try:
        guess = int(input("guess a number [1-10] "))
    except ValueError:
        print("invalid input mf!")
        

    if guess in range(1,11):                    
        if guess == num:
            print("correct!!")
        elif guess > num:
            print("too high")
        else:
            print("too low")
    else:
        print("range must be within 1-10\n")