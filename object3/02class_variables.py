# We define a class CoffeeMachine of which the virtual objects hold the amount of beans and amount of water.
# Both are defined as a number (integer). 
# We may then define methods that add or remove beans.

# We do the same for the variable water.

class CoffeMachine:
    name = ''
    beans = 0
    water = 0
    def __init__(self, name, beans, water) -> None:
        self.name = name
        self.beans = beans
        self.water = water

    def add_beans(self):
        self.beans += 1

    def remove_beans(self):
        self.beans -= 1

    def add_water(self):
        self.water += 1

    def remove_water(self):
        self.water -= 1

    def print_state(self):
        print(f'name: {self.name}, beans: {self.beans}, water: {self.water}')
        self.add_beans()
        print('')
        print(f'name: {self.name}, beans: {self.beans}, water: {self.water}')


james_coffee = CoffeMachine('James coffee', 1, 1)
# call object method
james_coffee.print_state()