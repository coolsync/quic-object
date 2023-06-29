
"""
Problem 11: Write a function dups to find all duplicates in the list.

dups([1, 2, 1, 3, 2, 5])
[1, 2]
"""

def duplicate(num_list):
    new_list = []
    for i in num_list:
        if i not in new_list:
            new_list.append(i)
                # new_list.append(y)
    # print(new_list)

duplicate([1, 2, 1, 3, 2, 5])
