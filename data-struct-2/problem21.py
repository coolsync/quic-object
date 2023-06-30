"""
Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

$ python wrap.py she.txt 30
I'm sure that the shells are s
eashore shells.
So if she sells seashells on t
he seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the sea
shore;
"""

def wraps(filename, width):
    for x in open(filename):
        x =  x[:width] + '\n' + x[width:]
        print(x)

wraps('./she.txt', 30)