"""
Problem 14: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.

unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
["python", "java"]
"""

def unique(str_list, key):
    str_list.sort(key = key, reverse=True)
    print(str_list)
    ls1 = []
    for s in str_list:
        ls1.append(s.lower())
    print(ls1)

    ls1 = set(ls1)
    print(list(ls1))

unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
