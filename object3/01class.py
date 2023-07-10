# create class
class User:
    # variables
    name = ""
    def __init__(self, name):
        self.name = name

    # methods
    def sayHello(self, content):
        print(f'{self.name} say: {content}')

#  create object
james = User('James')
david = User('David')
eric = User('Eric')

# call method
james.sayHello('fuck off')
david.sayHello('dubby')
eric.sayHello('good bye')