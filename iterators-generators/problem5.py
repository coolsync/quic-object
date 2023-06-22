# Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.

import os
def find_file(dir):
    for (root,dirs,files) in os.walk(dir):
        for file in files:
           if file[-3:] == '.py':
               yield file

def read_lines(file):
    result = []
    for line in open(file):
       result.append(line)
    return result

# n express line numbers 
n = 0
for file in find_file('./'):
    # for line in read_lines(file):
        # print(line)
    n += len(read_lines(file))

print(n)


# print(result)

    
    

