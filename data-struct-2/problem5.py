""" 
Problem 5: Write a function factorial to compute factorial of a number. 
Can you use the product function defined in the previous example to compute factorial?
factorial(4) = 24
1 * 2 * 3 * 4 = 24
"""
def factorial(num):
    # print(range(num))
    result = 1
    for i in range(num):
        i += 1
        result *= i
        # print(i)
    print(result)
# factorial(4)