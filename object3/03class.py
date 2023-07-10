class Animal:
    name = ""
    def __init__(self, name) -> None:
        self.name = name

    def walk(self):
        print(f'{self.name} wins')

rabbit = Animal('rabbit')
turtle = Animal('turtle')
turtle.walk()

