"""
Problem 13: Write a function lensort to sort a list of strings based on length.

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
['c', 'perl', 'java', 'ruby', 'python', 'haskell']
"""

def lensort(str_list):
    # aList = []
    # for s in str_list:
        # aList.append()
    str_list.sort(key=lambda x: len(x))
    return str_list

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
