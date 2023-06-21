# Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

# 问题3：编写一个函数findfiles，该函数递归地降低指定目录的目录树，并生成树中所有文件的路径。

# 列出目录下所有的目录和文件
# 遍历目录所有文件
# 获取dirctory and file absolute path
# 判断文件类型
# 如果是指定的dirctory, 将其中所有文件的路径放到一个list中
# print files list 


# 目标dirctory: /home/fun-coding/ssh
import os
def findfiles():
    filepaths = os.listdir('/home/fun-coding/')
    for filepath in filepaths:
        abs_path = '/home/fun-coding/' + filepath
        # print(abs_path)
        if os.path.isdir(abs_path) and abs_path == "/home/fun-coding/ssh":
            # pass
            # print(abs_path)
            in_filepath = os.listdir(abs_path)
            print(in_filepath)
            for filename in in_filepath:
                # print(filename)     
                if os.path.isfile("/home/fun-coding/ssh/" + filename):
                    print(filename)
                    
                    # print(filepath)
                    
            
# findfiles()

# root, dirs, files
root = '/home/fun-coding/ssh'
def fildfiles(root):
    filepaths = os.listdir(root)
    for filepath in filepaths:
        # print(filepath)
        if os.path.isfile(os.path.join(root, filepath)):
            # print(filepath)
            yield filepath


for file in fildfiles(root):
    print(file)

def findfiles(taget_dir):
    for (root, dirs, files) in os.walk(taget_dir):
        for file in files:
            yield file

for file in findfiles('/home/fun-coding/ssh'):
    print(file)
