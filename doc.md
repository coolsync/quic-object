
## Create file in py

- Create a fiel in the current directory or a specified directory
- create a file if not exists
- create a file with a date and time as its name
- create a file with permissions

range(101): don't 包括 last '101'


## object
先理解大概的think, 再理解details, last write code.

if not isinstance： 用于判断一个对象是否属于某个类。如果对象属于该类，则返回 True，否则返回 False。


## iterators
 You don’t have to worry about ...

## generator
你可以使用Python的os库中的`os.walk()`函数来递归查找指定目录下的所有文件，并生成它们的路径。以下是一个可行的实现： 

#### Problem 3
```python
import os

def findfiles(directory):
    """
    递归查找指定目录下的所有文件，并生成它们的路径。
    :param directory: 要查找的目录路径
    :return: 一个包含所有文件路径的生成器对象
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)
```

这个函数接受一个参数 `directory`，表示要查找的目录路径。在函数内部，我们调用 `os.walk()` 函数对该目录进行递归遍历，并使用一个嵌套循环遍历每个子目录下的文件。在内层循环中，使用 `os.path.join()` 函数连接文件所在目录和文件名，生成完整的文件路径，并使用 `yield` 语句将其作为生成器对象返回。通过这种方式，我们可以迭代返回所有文件路径，而不必一次性将所有文件路径存储在内存中。

你可以像下面这样使用这个函数来获取指定目录下的所有文件路径：

```python
for file in findfiles('/path/to/directory'):
    print(file)
```

注意替换掉代码中的 `/path/to/directory` 为你需要查找的目录路径。如果你需要将这些路径存储到列表中，可以使用 `list()` 函数将生成器对象转换为列表。
