# Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

def filter(pat, filenames):
    # result =[]
    for f in filenames:
        for line in open(f):
            if len(line) > 40:
                print(line, end="") 

# def grep(pattern, lines):
    # return [line for line in lines if len(pattern) > 40]



filter('body', ['./a.txt', './b.txt'])

