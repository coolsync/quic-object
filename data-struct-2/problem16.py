"""
Problem 16: Write a function extsort to sort a list of files based on extension.
extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
"""
def extsort(filenames):
    filenames.sort(key=lambda x: x.split('.')[1])
    return filenames

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))