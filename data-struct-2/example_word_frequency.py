"""
Returns frequency of each word given a list of words.

        >>> word_frequency(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
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
    # ValueError: too many values to unpack (expected 2)
    for x,y in word_frequency(read_words(filename)).items():
        print(x, y)
        

main('./she.txt')