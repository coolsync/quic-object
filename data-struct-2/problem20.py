"""
Problem 20: Implement unix command grep. 
The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
"""

"""
1. 遍历每一行， 从每一行中找到目标单词
"""
def grep(filename, word):
    for x in open(filename).readlines():
        if word in x:
            print(x)

grep('./she.txt', 'sure')