#VARIABLE SCOPE

#CASE 1
#local variable
#a function can have its own local variables.
name = "Zack"

def greet():
    name = "Ali"
    print(name)

greet()
print(name)


#CASE 2
#global variable
score = 10

def update_score():
    global score
    score = score + 5

update_score()
print(score)