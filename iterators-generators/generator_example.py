# 1. 生成无限整数序列
# 2. 生成前n个序列

def interges():
    i = 1
    while True:
        yield i
        i += 1

def squres():
    for i in interges():
        yield i * i

# print(list(squres()))
def take(n, seq):
    # 迭代器
    seq = iter(seq)
    
    resualt = []
    try: # extend
        for i in range(n):
            resualt.append(next(seq))
    except StopIteration:
        pass

    return resualt

print(take(5, squres()))

# squres: 表示 'function' object
# squres(): 表示 'function' execute
