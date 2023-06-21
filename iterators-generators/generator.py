def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


y = yrange(5)
print(next(y))
print(list(y))
print(list(y))


class yrange:
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


y = yrange(5)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# print(list(y))


class zrange:
    def __init__(self, n) -> None:
        self.n = n
    
    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
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

z = zrange(5)
print(list(z))
print(list(z))

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
    yrange(n)

y = yrange(5)
# print(list(y))
# print(list(y))

# 下面的例子说明了generator 对象上 __next__ 方法和yield interplay
def foo():
    print('begin')
    for i in range(3):
        print('before yield i = ', i)
        yield i
        print('after yield i = ', i)
    print('end')


f = foo()
print(next(f))
print(next(f))
print(next(f))
print(next(f))

