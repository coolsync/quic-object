# 5.3.1. Example: Reading multiple files

def cat(filenames):
    for f in filenames:
        # for line in open(f, 'r').readlines():
        for line in open(f):
            print(line, end="")

filenames = ['./a.txt', './b.txt']
# cat(filenames)

# AttributeError: 'str' object has no attribute 'read'

# with open('./a.txt', 'r') as fp:
    # for line in fp.readlines()

# 创建一个grep() function, 通过多个文件中找出指定的字符串, 即正则
def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end="")

# grep(pattern='body', filenames=filenames)

# 这两个程序有很多共同的代码。很难将公共部分移动到函数中。但有了发电机，就有可能做到这一点。


# 迭代生成每一行
def readlines(filenames):
    for f in filenames:
        for line in open(f):
            yield line

# 获取指定字符串的行
def grep(pattern, lines):
    return [line for line in lines if pattern in line]

# 打印指定行
def printlines(lines):
    for line in lines:
        print(line, end="")

# 合并上述function, 形成步骤
def main(pattern, filenames):
    lines = readlines(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

main('body', filenames=filenames)

