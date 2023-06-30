"""
Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

print(open('a.txt').read())
# elements are separated by ! and comment indicator is #
a!b!c
1!2!3
2!3!4
3!4!5
parse('a.txt', '!', '#')
[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
"""

def parse(filename, c1, c2):
    n1 = []
    for x in open(filename):
        if c2 not in x:
            n1.append(x.strip())
    print(n1)
    n2 = []
    for x in n1:
        x = x.split('!')
        n2.append(x)
    print(n2)
parse('a.txt', '!', '#')