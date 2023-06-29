# Problem 9: Write a function cumulative_product 
# to compute cumulative product of a list of numbers.
# unique([1, 2, 1, 3, 2, 5])
# [1, 2, 3, 5]

def unique(num_list):
    new_list = []
    for i in num_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique([1, 2, 1, 3, 2, 5]))
