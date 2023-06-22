# 一段英文文本词频

with open('./t.txt', 'r') as fp:
    words = fp.read().split()
    # print(len(words))
    for word in set(words):
        # print("{}--{}".format(word, words.count(word)))
        pass
    fp.close()


# 分割文本单词为list, 并去掉特殊符号
#   strip
# 去除一个word list 中重复word
# 将word与之对应的次数形成map
# 按照word map中value, 即出现的次数降序sd

import string
with open('./t.txt', 'r') as fp:
    words = [word.strip(string.punctuation).lower() for word in fp.read().split()]
    # print()
    words_index = set(words)
    words_map = {index: words.count(index) for index in words_index}

#  key=lambda x: words_list[x] -> 以value作为排序的依据
for word in sorted(words_map, key=lambda x: words_map[x], reverse=True):
    print("{}--{}".format(word, words.count(word)))