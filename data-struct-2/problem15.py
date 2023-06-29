"""
4 Write a function unique to find all the unique elements of a list.
unique([1, 2, 1, 3, 2, 5])
[1, 2, 3, 5] 
"""

def unique(a_list):
    # r = []
    # for x in a_list:
    #      for y in a_list:
    #           if x != y:
    #                r.append(x)
    new_list = []
    for x in a_list:
        if x not in new_list:
            new_list.append(x)        
    return new_list

print(unique([1, 2, 1, 3, 2, 5]))

# use sets reimplement unique function
def unique(a_list):
    a = set(a_list)
    # print(a)
    return list(a)



# def unique(num_list):


