"""
Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

a = array(2, 3)
a
[[None, None, None], [None, None, None]]
a[0][0] = 5
[[5, None, None], [None, None, None]]
"""

def array(a, b):
    new_list = [];
    for i in range(a):
        new_list.append([None for j in range(b)])
    return new_list

def create_2d_array(rows, cols):
    array = [[None] * cols for _ in range(rows)]
    return array

print(create_2d_array(1, 3))

a = array(2, 3)
print(a)
a[0][0] = 5
print(a)
