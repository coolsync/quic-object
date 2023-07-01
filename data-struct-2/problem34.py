"""

Problem 36: Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
[['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
Problem 37: Write a function valuesort to sort values of a dictionary based on the key.

valuesort({'x': 1, 'y': 2, 'a': 3})
[3, 1, 2]
Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

invertdict({'x': 1, 'y': 2, 'z': 3})
{1: 'x', 2: 'y', 3: 'z'}
"""



# 1. create 词频 function, 从单词列表中统计单词出现的个数
# 2. 从一个文件中读取所有单词， 返回单词列表
# 3. 打印每个单词出现的次数

def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    # print(frequency)
    return frequency

def read_words(filename):
    return open(filename).read().split()


def main(filename):
    # 出现 ValueError: too many values to unpack (expected 2)， items() 忘记加
    for x,y in word_frequency(read_words(filename)).items():
        print(x, y)

"""
Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.
问题 34: 改进上述程序，按出现次数降序打印单词。

"""
######################### 改进部分
def main(filename):
    # method 1
    new_list = []
    for x,y in word_frequency(read_words(filename)).items():
        new_list.append((x, y))
    new_list.sort(key=lambda x: x[1], reverse=True) # 升序
    print(new_list)

    # method 2
    order_dict = dict(sorted(word_frequency(read_words(filename)).items(), key=lambda x: x[1], reverse=True))
    print(order_dict)
#########################
main('./she.txt')