# Problem 8: Write a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

# it = iter(range(5))
# x, it1 = peep(it)
# print(x, list(it1))
# 0 [0, 1, 2, 3, 4]

it = iter(range(5))
# print(next(it))
# print(next(it))

def peep(it):
    a = list(it)
    return a[0], iter(a)
    
x, y = peep(it)
print(x, list(y))
    