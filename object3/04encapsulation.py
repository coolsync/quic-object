name = ['a', 'b', 'c', 'd']
print(name[-5:-1:1])
tpl1 = (60)
tpl2 = (60,)
print(type(tpl1), type(tpl2))

a = [0, 1, 2, 1.0, 2.0, 3.0, False, True, bool(1), 'a', 'b', 'c']
print(a)

#4. 这里有一个数据：name = ['猪八戒','孙悟空','嫦娥','杨戬','花木兰']
# 4.1 在这个数据最后面依次添加孙尚香，刘禅
# 4.2 在这个数据下标为3的地方添加安琪拉，下标为5的地方添加亚瑟
# 4.3 如果我有一个name2 = [李白，玄策，凯，云中君] 可是我想合并到name 怎么操作呢？
# 4.4 猪八戒和嫦娥吵架了，嫦娥需要离家出走回娘家，怎么解决？
# 4.5 我忘记了下标为5的是谁了，我想移出他怎么办？
# 4.6 我想移出最后一个人怎么操作？
# 4.7 嫦娥回娘家了，我想把她所在的位置交给李元芳，怎么操作呢？
# 4.8 我想查一下 凯是不是在我的数据当中，怎么操作？

# 4.1 在这个数据最后面依次添加孙尚香，刘禅
name = ['猪八戒','孙悟空','嫦娥','杨戬','花木兰']
name.append('孙尚香')
name.append('刘禅')
# name.extend(['孙尚香', '刘禅'])
# print(name)

# 4.2 在这个数据下标为3的地方添加安琪拉，下标为5的地方添加亚瑟
name.insert(3, '安琪拉')
name.insert(5, '亚瑟')
# print(name)

# 4.3 如果我有一个name2 = [李白，玄策，凯，云中君] 可是我想合并到name 怎么操作呢？
name2 = ['李白', '玄策', '凯', '云中君']
name.extend(name2)
# print(name)
# ['猪八戒', '孙悟空', '嫦娥', '安琪拉', '杨戬', '亚瑟', '花木兰', '孙尚香', '刘禅', '李白', '玄策', '凯', '云中君']

# 4.4 猪八戒和嫦娥吵架了，嫦娥需要离家出走回娘家，怎么解决？
# n = name.index('嫦娥')
# del(name[n])
# name.pop(n)
# name.remove('嫦娥')
# print(name)

# 4.5 我忘记了下标为5的是谁了，我想移出他怎么办？
del(name[5])
# print(name)

# 4.6 我想移出最后一个人怎么操作？
name.pop()
# print(name)

# 4.7 嫦娥回娘家了，我想把她所在的位置交给李元芳，怎么操作呢？
name.insert(name.index('嫦娥'), '李元芳')
# print(name)

# 4.8 我想查一下 凯是不是在我的数据当中，怎么操作？
if '凯' in name:
    print('凯 is in name list')

#5.这里有一个学生成绩数据：achievementList = [43,23,12,16,12,34,54,76,34,23,54,35,78]
# 5.1 我需要知道这个数据从小到大的顺序，以及分数最低是多少
# 5.2 我需要知道这个数据从大到小的顺序，以及分数最大是多少
# 5.3 我需要知道这个数据有多少个同学的数据,可以帮我查一下吗
# 5.4 可以帮我统计一下 54分的有多少吗？

# 5. it is scores of a students data in here:
achievementList = [43,23,12,16,12,34,54,76,34,23,54,35,78]

# 5.1 我需要知道这个数据从小到大的顺序，以及分数最低是多少
a = sorted(achievementList)
print(f'achievementList from small to big order: {a}, score less: {a[0]}')

# 5.2 我需要知道这个数据从大到小的顺序，以及分数最大是多少
a = sorted(achievementList, reverse=True)
print(f'achievementList from big to small order: {a}, max score: {a[0]}')

# 5.3 我需要知道这个数据有多少个同学的数据,可以帮我查一下吗
print(f'how much students data: {len(a)}')

# 5.4 可以帮我统计一下 54分的有多少吗？ use count function
# a.count(54)
print(f'54 scores students: {a.count(54)}')
b = ['a', 'b', 'c', 'd', 'e', 'c']
print(b.count('a'))


# 6.什么是元组？ 如何定义一个元组？
# 元组是一种不可变的有序数据集合，用于存储多个元素。
# 你可以使用圆括号来定义一个元组，并通过索引访问其中的元素。
# tuple = (50, 60)

# 7. 我这里有一个数据 tup1 = (20,40,50,60,20,40,30,80)
# 7.1 查询数据里面关于50的个数
# 7.2 查询第一个50的下标
# 7.3 我这里还有数据tup2 = (30,49,20,43,45,65) 怎么合并到tup1里面呢？
# 7.4 可以帮我看一下合并之后的数据有多少吗？

tup1 = (20,40,50,60,20,40,30,80)

# 7.1 查询数据里面关于50的个数
n = tup1.count(50)
print(n)
# 7.2 查询第一个50的下标
n = tup1.index(50)
print(tup1[n])
# 7.3 我这里还有数据tup2 = (30,49,20,43,45,65) 怎么合并到tup1里面呢？
tup2 = (30,49,20,43,45,65)
tup1 += tup2
print(tup1)

# 7.4 可以帮我看一下合并之后的数据有多少吗？
print(f'after combination: {len(tup1)}')


# 8.什么是字符串? 
# 8. 我这里有一个数据 str1 = 'thank you for your kind words and encouragement, teacher. i will strive to approach problems calmly and take step-by-step learning. i will do my best. thank you for your support!'
# 8.1  可以帮我统计一下 a,b,c,d字母出现了几次吗
# 8.2  可以帮我将每个单词首字母大写吗？
# 8.3  可以帮我将所有的字母转大写吗？
# 8.4  可以帮我将you 修改为your吗？

str1 = 'thank you for your kind words and encouragement, teacher. i will strive to approach problems calmly and take step-by-step learning. i will do my best. thank you for your support!'

a_count = str1.count('a')
b_count = str1.count('b')
c_count = str1.count('c')
d_count = str1.count('d')

print(f'a appear counts: {a_count}')
print(f'b appear counts: {b_count}')
print(f'c appear counts: {c_count}')
print(f'd appear counts: {d_count}')

# 8.2  可以帮我将每个单词首字母大写吗？
str2 = str1.capitalize()
print(str2)

# 8.3  可以帮我将所有的字母转大写吗？
str2 = str1.title()
print(str2)

# 8.4  可以帮我将you 修改为your吗？
# str_list = str1.split(' ')
# for s in str_list:
str2 = str1.replace('you', 'your', -1)
print(str2)
    
