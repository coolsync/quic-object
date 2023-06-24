class Employee:
    company = 'transport'
    def __init__(self, name, age):  # __init__ 是一个类的构造方法, auto call
        self.name = name
        self.age = age

    def hello(self):    
        print(f'{self.name}, {self.age}')

    @classmethod
    def which_company(cls):
        print(cls.company)

    @staticmethod
    def help_func():    # no cls param
        print("i'm a static method")

bob = Employee('bob', 34)
jerry = Employee('jerry', 30)
bob.hello()
bob.which_company()

# modify class variable
Employee.company = 'computer'
jerry.which_company()
jerry.help_func()
