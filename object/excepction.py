import sys
# import parse_cvs
# import io
# import os
# def main():
#     filename = sys.argv[1]
#     try:
#         with open(filename, 'r') as fp:
#             for line in fp.readlines():
#                 print(line)
#             fp.close()
#         # pass
#     except IOError:
#         print('the file is 不存在', filename, os.EX_IOERR)
#         os._exit(1)

# main()

try:
    print("a")
    raise Exception("doom")
except:
    print("b")
else:
    print("c")
finally:
    print("d")

def f():
    try:
        print("a")
        return  #  在 except 前 return 不起作用，
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()