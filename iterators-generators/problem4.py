# Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import os
def findfiles(target):
    for (root, dirs, files) in os.walk(target):
        for file in files:
            filename = os.path.join(root, file)
            # print(file[-3:])
            # if filename[-3:] == ".py":
            if filename.endswith('.py'):
                # print(file)
                yield filename
            

filepath = os.path.abspath('./')    # apply system absolute path
print(filepath)
for file in findfiles(os.path.abspath('./')):
    print(file)