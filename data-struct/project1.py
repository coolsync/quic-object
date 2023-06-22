import string

# open a file
# spit a text to word list, drop special sysbol
# remove duplicate words
# create map, index words, value word appear counts

filename = './t.txt'
with open(filename, 'r') as fp:
    words = [word.strip(string.punctuation).lower() for word in fp.read().split()]
    words_set = set(words)
    # print(words_set)
    words_dict = {index: words.count(index) for index in words_set}
    # print(words_dict)

words1 = sorted(words_set, key=lambda x: words_dict[x], reverse=True);

# order down lamdal
# for word in [words_list, key=lambda x: words_map[x], reverse=True]:
    # print("{}-{}".format(word, words.count(word)))

# for word in sorted(words_set, key=lambda x: words_dict[x], reverse=True):
for word in sorted(words_dict, key=lambda x: words_dict[x], reverse=True):
    print("{}--{}".format(word, words.count(word)))
