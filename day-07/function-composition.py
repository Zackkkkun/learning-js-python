#function inside another function
def multiply(a, b):
    return a * b

x = multiply(4, 5)
y = multiply(x, 2)

print(y)