'''

python开发基础36-函数的定义&规则

'''


def myLoop(n):
    '''
    函数的第一行语句可以选择性使用文档字符串用于存放函数的说明
    :param n: 循环次数
    :return: 无return值
    '''
    for i in range(n):
        print(i, end=' ')


myLoop(12)

print(myLoop.__doc__)      #可使用.__doc__打印函数的说明

'''
Outputs:

0 1 2 3 4 5 6 7 8 9 10 11 
    函数的第一行语句可以选择性使用文档字符串用于存放函数的说明
    :param n: 循环次数
    :return: 无return值

'''


