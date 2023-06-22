class yrange:
    def __init__(self, n) -> None:
        self.i = 0;
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i         
        else:
            raise StopIteration()
        
y = yrange(5)
print(next(y))

# print(list(yrange(3)))
# print(list(yrange(3)))
print(list(y))
print(list(y))


class zrange:
    def __init__(self, n) -> None:
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n) -> None:
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i    
        else: 
            raise StopIteration()

# print(list(zrange(5)))
# print(list(zrange(5)))
z = zrange(5)
print(list(z))
print(list(z))


class xrange:
    def __init__(self, n) -> None:
        self.i = n
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            i = self.i
            self.i -= 1
            return i         
        else:
            raise StopIteration()

x = xrange(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
