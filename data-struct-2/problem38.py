"""
问题 38： 编写一个函数来交换字典中的键和值。为简单起见，假设所有值都是唯一的。invertdict

invertdict({'x': 1, 'y': 2, 'z': 3})
{1: 'x', 2: 'y', 3: 'z'}
"""

def invertdict(d1):
    n = {y: x for x, y in d1.items()}
    print(n)

invertdict({'x': 1, 'y': 2, 'z': 3})

def f(a, b): print(locals())
f(1, 2)