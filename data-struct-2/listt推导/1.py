r = [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
print(r)

ls = []
for x in range(5):
    for y in range(x):
        if (x+y)%2 == 0:
            ls.append((x, y))

print(ls)

# zip([1, 2, 3], ["a", "b", "c"])
# r = [(x, y) for x in [1, 2, 3] for y in ["a", "b", "c"]]
# print(r)
# ls = []
# for x in [1, 2, 3]:
    # ls.append((x,))
# for x in ['a', 'b', 'c']:
    # ls.append()

num = [1, 2, 3]
s = ['a', 'b', 'c']

n = len(num)
ls = []
while n > 0:
    n -= 1
    ls.append((num[n], s[n]))
ls.reverse()

print(ls)