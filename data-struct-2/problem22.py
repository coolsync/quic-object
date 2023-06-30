""" 
Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program wordwrap.py that works like wrap.py, but breaks the line only at the word boundaries?

上面的换行程序不太好，因为它在任何单词的中间换行。你能写一个新程序wordwrap.py吗？它的工作原理和wrap.py一样，但只在单词边界处换行？

$ python wordwrap.py she.txt 30
I'm sure that the shells are
seashore shells.
So if she sells seashells on
the seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the
seashore; 

She sells seashells on the sea
shore;

The shells that she sells are 
seashells I'm sure.

So if she sells seashells on t
he seashore,

I'm sure that the shells are s
eashore shells.
"""


def wraps(filename, width):
    for line in open(filename):
        # x =  x[:width] + '\n' + x [width:]
        line = line.split()
        print(line)

wraps('./she.txt', 30)