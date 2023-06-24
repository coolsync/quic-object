class MyStuff():
    def __init__(self) -> None:
        self.juzi = 'i like juzi'
    
    def print_info(self):
        print('this is common method')

thing = MyStuff()
print(thing.juzi)
thing.print_info()