"""
Problem 25: Python provides a built-in function that applies a function to each element of a list. Provide an implementation for using list comprehensions.
map

def square(x): return x * x

map(square, range(5))
[0, 1, 4, 9, 16]
"""

def square(x): return x * x

def map(square, n):
    newlist = []
    for i in n:
        newlist.append(square(i))
    print(newlist)

map(square, range(5))