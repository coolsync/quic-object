"""
问题 36： 编写一个程序以在给定的单词列表中查找字谜。如果一个单词可以通过重新排列另一个单词的字母来形成，则两个单词称为字谜。例如，“吃”，“吃”和“茶”是字谜。

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
[['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
"""

def find_anagrams(words):
    anagram_groups = []

    while words:
        word = words.pop(0)
        print(word)
        anagram_group = [word]
        print(anagram_group)
        for i in range(len(words) - 1, -1, -1):
            if sorted(words[i]) == sorted(word):
                anagram_group.append(words.pop(i))

        anagram_groups.append(anagram_group)

    return anagram_groups

word_list = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
result = find_anagrams(word_list)
print(result)
# for x in range(5, -1, -1):
    # print(x)

"""AI is creating summary for 
#######################解释############################
#######################解释############################
#######################解释############################
输出结果：

[['eat', 'ate', 'tea'], ['done', 'node'], ['soup']]
在上述代码中，我们定义了一个名为find_anagrams的函数来查找给定单词列表中的字谜（anagrams）。我们创建了一个空列表anagram_groups来存储找到的字谜分组。

我们使用一个循环来遍历输入单词列表。在每次迭代中，我们从列表中弹出一个单词word，并创建一个初始的字谜分组anagram_group，其中包含当前单词。

然后，我们通过倒序遍历剩余的单词列表来检查是否有其他单词是word的字谜。我们使用sorted()函数对两个单词进行排序，并比较它们是否相等。如果两个单词是字谜关系，则将该单词从列表中移除，并将其添加到当前字谜分组中。

完成内部循环后，我们将anagram_group添加到anagram_groups列表中。然后，我们继续下一次迭代直到列表为空。

最后，我们打印输出result，即找到的字谜分组列表。每个子列表表示具有字谜关系的单词组。

#######################解释############################
#######################解释############################
#######################解释############################
"""

