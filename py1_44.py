'''

python开发基础44-py文件不同的执行方式

'''

def sum(a,b):
    return a+b


if __name__ == '__main__':     #当前文件被作为主程序执行
    mySum = sum(1, 2)
    print('1 + 2 =', mySum)

    print('The module name is', __name__)





'''
Outputs:

1 + 2 = 3
The module name is __main__


'''





