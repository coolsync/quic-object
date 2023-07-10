# encapsulation in python
"""
In an object oriented python program, 
you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as encapsulation.
"""

class Car:
    # class variable
    __maxspeed = 0
    __name = ""
    
    # init method
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    # common method
    def drive(self):
        print(f'driving... maxspeed: {str(self.__maxspeed)}')

redcar = Car()
redcar.drive()  # 200
redcar.__maxspeed = 10  # private variable not change
redcar.drive() # 200

class Car:
    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def dirve(self):
        print(f'driving, max speed: {str(self.__maxspeed)}')

    # if you to change the private variable, use setter method
    def setMaxSpeed(self, max_speed):
        self.__maxspeed = max_speed

red_car = Car()
red_car.dirve()
red_car.setMaxSpeed(320)
red_car.dirve()

"""
Method Overlaoding
"""
class Human:
    # name = ''
    # def __init__(self, name) -> None:
    #     self.name = name

    def sayHello(self, name=None):
        if name is not None:
            print(f'hello, {name}')
        else:
            print('hello')

# create an instance
julia = Human()
# call a method
julia.sayHello()
# call a method with an parameter
julia.sayHello('julia')

"""
python class inheritance

"""
class User:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(f'{self.name}')

class Programs(User):
    def __init__(self, name):
        self.name = name

    def doWitch(self):
        print('at the moment, do python')

u1 = User('bob')
u1.printName()

u2 = Programs('paul')
u2.printName()  # this method from class User inheritance
u2.doWitch()
    
"""
Polymorphism
polymorphism is implemented through inheritance and method overriding, enabling objects of different types to respond to the same messge differently.
"""

# 1. Polymorphism with a function
# 
