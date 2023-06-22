# Problem 10: Implement a function izip that works like itertools.izip.
# for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
#     print(x, y)

# a 1
# b 2
# c 3

def izip(a, b):
    for x, y in zip(a, b):
        yield (x, y)
print(list(izip(["a", "b", "c"], [1, 2, 3])))

for x, y in izip(["a", "b", "c"], [1, 2, 3]):
    print(x, y)

def izip(a, b):
    n = 0;
    for x in a:
        yield(x, b[n])
        n += 1

print(list(izip(["a", "b", "c"], [1, 2, 3])))

for x, y in izip(["a", "b", "c"], [1, 2, 3]):
    print(x, y)