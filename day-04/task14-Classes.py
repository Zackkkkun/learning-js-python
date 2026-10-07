"""----------------------------------------------------------
Task 14 — Classes

Write code that:

Defines a class Car with __init__(self, brand, speed) that stores both as attributes
Adds a method drive(self) that returns f"{self.brand} is driving at {self.speed} km/h"
Creates an object my_car = Car("Toyota", 120)
Prints my_car.drive()

----------------------------------------------------------"""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return f"{self.brand} is driving at {self.speed} km/h"

my_car = Car("Toyota", 120)
print(my_car.drive())