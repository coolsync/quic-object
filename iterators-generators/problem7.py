# Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines.

# open file, yield file

# read line in a file

# according to n liens write to single file
import os
a = ['aaaaa', 'bbb', 'cccc', 'aaaaa', 'bbb', 'cccc', '555', '666']
n = 0
for i in range(0, len(a), 3):
    n += 1
    with open(os.path.join('./', f'{n}.txt'), 'w') as f:
        for line in a[i:i+3]:
            f.write(line + '\n')

            
