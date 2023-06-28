# 实现built-in functions min and max
""" 
Problem 7: 
Python has built-in functions min and max to compute minimum and maximum of a given list. 
Provide an implementation for these functions. 
What happens when you call your min and max functions with a list of strings?
"""

def min(num_list):
    # min_num = 0
    return sorted(num_list)[0]
print(min([3, 1, 2, 3, 1]))

def max(num_list):
    return sorted(num_list)[-1]
print(max([3, 1, 2, 3, 1]))


def min(num):
    min_element = num[0]
    for i in num:
        if min_element >= i: min_element = i    
    return min_element

def max(num):
    min_element = num[0]
    for i in num:
        if min_element <= i: min_element = i    
    return min_element

def min_and_max(num):
    min_num = num[0]
    max_num = num[0]
    for i in num:
        if min_num >= i: min_num = i
        if max_num <= i: max_num = i 
    return min_num, max_num
print(min_and_max([10, 2, 1, 3, 9, 7]))