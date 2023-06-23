# Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

import os
# 指定目录，找出所有文件
def opendir(dir):
    for (root, dirs, files) in os.walk(dir):
        for file in files:
            if file[-3:] == '.py':
                yield os.path.join(root, file)
# read line in a file 
def readlines(f):
    result = []
    for line in open(f):
        line = line.strip()
        # print(line)
        if not line.startswith('#'):
                    if  not line.endswith('\n'):
                        print(line)
                        result.append(line) # line.strip() 去掉空行

    # for v in result:
    # text = open(f)
    return result 
    
# 将所有的列表元素放到一个集合中，然后根据固定的大小分割列表，并放入一系列单独的文件
# according to n liens write to single file
import itertools
def main():
    n = 0
    # dir = opendir('./')

    result = []
    for file in opendir('./'):
        result += readlines(file)

    # print(dir)
    # print(result)
    # for i in result:
    #     print(i)
    for i in range(0, len(result), 10):
        n += 1
        with open(os.path.join('./', f'{n}.txt'), 'w') as f:
            for line in result[i:i+10]:
                f.write(line + '\n')        

main()
    # while True:

    # for i in range(0, len(a), 3):
    #     n += 1
    # with open(os.path.join('./', f'{n}.txt'), 'w') as f:
    #     for line in a[i:i+3]:
    #         f.write(line + '\n')        

# a = ['aaaaa', 'bbb', 'cccc', 'aaaaa', 'bbb', 'cccc', '555', '666']


            
