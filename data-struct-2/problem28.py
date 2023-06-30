"""
Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
0 a
1 b
2 c
"""

def enumerate(alist):
    n = 0
    new_list = []
    for x in alist:
        new_list.append((n,x))
        n += 1
    return new_list

for index, item in enumerate(['a', 'b', 'c']):
    print(index, item)
