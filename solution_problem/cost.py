a = '3 4 0 7 2 1 1 9 8 9 1 2 2 7 1 5 1 1'
a = set(a.split(' '))
a = list(a)
a.sort(key=lambda x: x)
print(a)
# b = [v for v in list(a)]