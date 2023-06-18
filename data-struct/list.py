fruit = ['apple', 'oragin']
fruit.insert(1, 'lanpa')    # add a element
print(fruit)


num_list = [3, 2, 1, 4, 5, 7, 1, 1]
print(sorted(num_list, reverse=True))

# Return a new list containing all items from the iterable in ascending order.
# A custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the result in descending order.
num = ['1', '2', '3']
addr = ['g', 'p', 'c']
for a, b in zip(num, addr): print(f'{a} is {b}')

import time

t0 = time.clock_gettime(time.CLOCK_MONOTONIC)
a = []
for n in range(1, 20000000): a.append(n)
print(f'cost time: {time.clock_gettime(time.CLOCK_MONOTONIC) - t0}')

t0 = time.clock_gettime(time.CLOCK_MONOTONIC)
b = [n for n in range(1, 20000000)]
print(f'cost time: {time.clock_gettime(time.CLOCK_MONOTONIC) - t0}')


a = [i**2 for i in range(1, 6)]
b = [j*2 for j in range(1, 6)]
c = [j for j in range(1, 6) if j % 2 == 0]
# d = [l.to_upper() for l in range("abcdefg")]
d = [l.upper() for i, l in zip(range(1,8), "abcdefg")]
print(d)

# map
a ={i:i+1 for i in range(1, 6)}
b= {i:j for i, j in zip(range(1, 6), "abcde")}
c = {i:j.upper() for i, j in zip(range(1, 6), "abcde")}
print(c)

# 列出 list 序号
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i, l in enumerate(letter): print(f'{l} {i}')
