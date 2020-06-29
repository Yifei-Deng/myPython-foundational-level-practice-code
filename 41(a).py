'''

python开发基础41-变量作用域

'''

total = 0
def sum(a,b):
    total = a + b         #函数内部的局部变量的名字如果和全局变量相同，则局部变量会暂时屏蔽全局变量，所以对局部变量的更改并不会影响全局变量
    print("Inside the function, the local variable 'total' equals to {}.".format(total))
    return total

print('The return value of the function is {}.'.format(sum(5,4)))
print("The global variable 'total' equals to {}.".format(total))



'''
Outputs:

Inside the function, the local variable 'total' equals to 9.
The return value of the function is 9.
The global variable 'total' equals to 0.

'''


