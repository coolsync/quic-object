# 2: Python has a built-in function sum to find sum of all elements of a list. Provide an implementation for sum.

# 有一个能够计算所有元素之和的built-in function sum, 实现这个sum function
# print(sum(num))
def sum(num):
    result = 0
    for i in num:
        result += i
    return result 
     
num = [1, 2, 3, 4]
print(sum(num))

# num = (1, 2, 3, 4)
# print(sum(num))
# print(sum)

# 3. 实现String之间的相加 
def sum(num):
    result = ''
    for i in num:
        result += i
    return result 
print(sum(["hello", "world"]))

# TypeError: can only concatenate str (not "int") to str

# 4. Write a function reverse to reverse a list. Can you do this without using list slicing?

def reverse(num):
    n = len(num)
    num_list = []
    while n > 0:
        n -= 1
        num_list.append(num[n])
    return num_list

num = [1, 2 ,3, 4]
print(reverse(reverse(num)))


# 实现built-in functions min and max
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
