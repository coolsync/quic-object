# Problem 6: Write a function to compute the total number of lines of code, 
# ignoring empty and comment lines, in all python files in the specified directory recursively.
# empty
# if line == ''

# line = "write a function"
# if '#' in line:
#     print(line)

import os
def find_file(dir):
    for (root,dirs,files) in os.walk(dir):
        for file in files:
           if file[-3:] == '.py':
               yield os.path.abspath(file)

# print(list(find_file('./')))
def read_lines(f):
    result = []
    for line in open(f):
       result.append(line)
    return result

# print(read_lines(list(find_file('./'))))

n = 0
n1 = 0
for f in find_file('./'):
    for line in read_lines(f):
        n1 += len(line)
        if not '#' in line or line == '':
            # print(line)
            n += len(line)

print(n, n1)
print(f'{n}, {n1}')   

# main(find_file('./'))
# TypeError: expected str, bytes or os.PathLike object, not generator