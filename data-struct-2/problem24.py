"""
Problem 24: Provide an implementation for function using list comprehensions.zip

zip([1, 2, 3], ["a", "b", "c"])
[(1, "a"), (2, "b"), (3, "c")]
"""

num = [1, 2, 3]
s = ['a', 'b', 'c']

n = len(num)
ls = []
while n > 0:
    n -= 1
    ls.append((num[n], s[n]))
ls.reverse()

print(ls)
