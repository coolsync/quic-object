"""
问题 37： 编写一个函数以根据键对字典的值进行排序。valuesort

valuesort({'x': 1, 'y': 2, 'a': 3})
[3, 1, 2]
"""

def valuesort(my_dict):
    # sorted(key=lambda x: my_dict[0])
    # keys = my_dict.keys()
    n = sorted(my_dict.items(), key=lambda x: x[0])
    print(n)
    print([x[1] for x in n])

valuesort({'x': 1, 'y': 2, 'a': 3})