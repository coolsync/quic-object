""" 
Problem 8: 
Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. 
Write a function cumulative_sum to compute cumulative sum of a list. 
Does your implementation work for a list of strings?
"""


# cumulative sum of [a, b, c, ...] 正如 [a, a+b, a+b+c, ...]
# [1, 2, 3]
# [1, 1+2, 1+2+3]
# n = len(list)
# for i range(n):
#     result.append(sum(list[:n-1-i]))
# re reverse(list)


# def cumulative(num_list):

# 将list按照给定的大小分割成多个小list
# group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
# [[1, 2, 3, 4], [5, 6, 7, 8], [9]]


# result = []
# for i in [0, len(list), n]:
#     result.app(list[i:i+n])

# n = [1, 2, 3, 4]
# print(n[1:3])

def group(a_list, size):
    result = []
    for i in range(0, len(a_list), size):
        result.append(a_list[i:i+size])
        print(i)
    return result

print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

# for i in range(0, 9, 3):
#     print(i)
# i i+size
# 0   3
# 3   6
# 6   9