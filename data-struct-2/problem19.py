"""

Problem 19: 
Implement unix commands head and tail. 
The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.

"""

import sys
# def reverse_line():
#     filename = './' + sys.argv[1]
#     print(filename)
#     # return len(open(filename).readlines()) # return txt lines
#     # n = len(open(filename).readlines())
#     new_list = []
#     for line in open(filename):
#         new_list.append(line.strip())
#     for i in new_list[::-1]:
#         print(i)
# reverse_line()


# def linecount(filename):
#     return len(open(filename).readlines())

# head -n filename
def special_line():
    command = sys.argv[1]
    n = int(sys.argv[2][1])
    filename = './' + sys.argv[3]
    lines = open(filename).readlines()
    line_len = len(lines)

    if command == 'head':
        for i in range(n):
            print(lines[i])
    
special_line()





