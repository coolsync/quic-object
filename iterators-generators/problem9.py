print(list(enumerate(['a', 'b', 'c'])))

for (x, y) in enumerate(['a', 'b', 'c']):  # return tuple
    print(x, y)


def my_enumerate(li):
    i = 0
    for v in li:
        # print(i)
        yield (i, v)
        i += 1

my_enumerate(['a', 'b', 'c'])
print(list(my_enumerate(['a', 'b', 'c'])))

for i in my_enumerate(['a', 'b','c']):
    print(i)

# ValueError: not enough values to unpack (expected 2, got 1)
# python list only print value, can't print index

                        