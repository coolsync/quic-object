# 假设我们想找到前10个（或任意n个）pythogorian三元组。如果x*x + y*y == z*z，则三元组（x，y，z）称为pythogorian三元组。

a = (x*x for x in range(10))
# print(sum(a))

a = ((x, y, z) for x in range(10) for y in range(10) for z in range(10) if x*x + y*y == z*z)
print(len(list(a)))

# 根据iterator function, 生成generator object， 返回list
def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            # print('')
            result.append(next(seq))
    except StopIteration:
        pass
    
    return result

print(take(5, seq=a))