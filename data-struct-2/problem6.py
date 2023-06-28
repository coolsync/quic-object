"""
Problem 6: 
Write a function reverse to reverse a list. 
Can you do this without using list slicing?

reverse([1, 2, 3, 4])
[4, 3, 2, 1]
reverse(reverse([1, 2, 3, 4]))
[1, 2, 3, 4]
"""

def reverse(num_list): # use slicing
    n = len(num_list)
    # new_list = []
    # for i in range(n):
    #     new_list.append(num_list[n-i-1])
    # return new_list
    return [num_list[n-i-1] for i in range(n)]
print(reverse(reverse([1, 2, 3, 4])))

def reverse(num):
    n = len(num)
    num_list = []
    while n > 0:
        n -= 1
        num_list.append(num[n])
    return num_list

num = [1, 2 ,3, 4]
print(reverse(reverse(num)))