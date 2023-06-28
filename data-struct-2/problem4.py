""" 
Problem 4: Implement a function product, to compute product of a list of numbers.
实现一个函数乘积，计算一系列数字的乘积。
product([1, 2, 3]) equal 6 
"""
def product(num_list):
    result = 1
    for i in num_list:
        result *= i
    print(result)
# product([1, 2, 3])
