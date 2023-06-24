# 1．使用这种方式写更多的歌进去，确保自己弄懂了传入的歌词是一个字符串列表。
# 2．将歌词放到另一个变量里，然后在类里使用这个新定义的变量。
# 3．试着看能不能给它加些新功能，不知道怎么做也没关系，只要试着去做就行，看会发生什么。尽管瞎折腾，弄坏了也没关系，反正程序不会觉得疼。
# 4．在网上搜索一下“object oriented programming”（面向对象编程），给自己洗洗脑。弄不懂也没关系，其实里边有一半的东西我也不理解。

class Song(object):
    lyrics = []
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


Song.lyrics = ["Happy birthday to you",
                   "I don′t want to get sued",
                   "So I′ll stop right there"]
happy_bday = Song(lyrics=Song.lyrics)

Song.lyrics = ["They rally around the family",
                        "With pockets full of shells"]
bulls_on_parade = Song(lyrics=Song.lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()