"""
Problem 23: Write a program center_align.py to center align all lines in the given file.

$ python center_align.py she.txt
  I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
       She sells seashells on the seashore;
"""

"""
1. 首先找出最长的一行
2. 然后根据最长的一行，动态地在每行前后加上同等的长度的空白字符
3. 将修改后每一行添加到新的list中
"""
def center_align(filename):
    n = ""
    for line in open(filename):
        if len(n) < len(line):
            n = line
    # print(n)
    # n = len(n) / 2
    # print(n)
    # newlist = []
    for line in open(filename):
        split_len = int((len(n) - len(line)) / 2) * ' '
        line = split_len + line + split_len
        print(line)


center_align('./she.txt')