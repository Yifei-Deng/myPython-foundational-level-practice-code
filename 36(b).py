'''

python开发基础36-函数的定义&规则

'''

def findMax(n):
    '''
     return [表达式]表示函数结束，return将返回值给函数调用方。
     如果函数不带return语句，相当于默认返回None

    :param n: a list
    :return: the maximum number in the given list
    '''
    a = max(n)
    return a


print(findMax([99,1,73,-100,0,0.3]))

'''
Output:

99

'''

