# Problem 3: What happens when the above sum function is called with a list of strings? 
# Can you make your sum function work for a list of strings as well.
# 3. 实现String之间的相加 
def sum(str_list):
    # result = ''
    # for i in str_list:
        # result += i
    # return result
    return ''.join(str_list) 
# print(sum(["hello", "world"]))


# 1: Write a function lensort to sort a list of strings based on length.
# lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
# ['c', 'perl', 'java', 'ruby', 'python', 'haskell']

def lensort(a_list):
    a_list.sort(key=lambda x: len(x))
    return a_list
print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))


# 4 Write a function unique to find all the unique elements of a list.
# unique([1, 2, 1, 3, 2, 5])
# [1, 2, 3, 5]

def unique(a_list):
    r = []
    for x in a_list:
         for y in a_list:
              if x != y:
                   r.append(x)
    return r

def unique(a_list):
    a = set(a_list)
    # print(a)
    return list(a)

print(unique([1, 2, 1, 3, 2, 5]))

# 5: Improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness.
# unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
# ["python", "java"]
def unique(a_list):
        a_list = [e.lower() for e in a_list]
        a_list.sort(key=lambda x: x.lower())
        print(a_list)
        a = set(a_list)
        print(a)
        a = list(a)
        return a
unique(["python", "javaj", "Python", "Java"])

