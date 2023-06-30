"""
Problem 30: Write a python function to parse csv (comma separated values) files.parse_csv

print(open('a.csv').read())
a,b,c
1,2,3
2,3,4
3,4,5
parse_csv('a.csv')
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""

print(open('a.csv').read())

def parse_csv(filename):
    new_list = []
    for line in open(filename):
        line = line.strip('\n')
        new_list.append(line.split(','))
    print(new_list)

parse_csv('a.csv')