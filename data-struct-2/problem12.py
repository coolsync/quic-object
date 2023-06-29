"""
Problem 12: Write a function group(list, size) 
that take a list and splits into smaller lists of given size.

group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]

"""
def group(num_list, size):
    aList = []
    for i in range(0, len(num_list), size):
        # print(i)
        aList.append(num_list[i:i+size])
    print(aList)

group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
