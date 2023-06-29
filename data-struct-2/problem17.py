""" 
Problem 17: Write a program reverse.py to print lines of a file in reverse order.

$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

$ python reverse.py she.txt
I'm sure that the shells are seashore shells.
So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
She sells seashells on the seashore; 
"""

import sys
def reverse_line():
    filename = './' + sys.argv[1]
    print(filename)
    # return len(open(filename).readlines()) # return txt lines
    n = len(open(filename).readlines())
    new_list = []
    for line in open(filename):
        new_list.append(line.strip())
    for i in new_list[::-1]:
        print(i)
reverse_line()


        

