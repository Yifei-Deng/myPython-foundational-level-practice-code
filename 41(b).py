'''

python开发基础41-变量作用域

'''

#  在函数内部读取一个全局变量时，不需要加global关键字。只有当需要给全局变量重新赋值(使用=号进行赋值)，才必须使用global。

total = 0
def sum(a,b):
    global total
    total = a + b
    print("Inside the function, the local variable 'total' equals to {}.".format(total))
    return total

print('The return value of the function is {}.'.format(sum(5,4)))
print("The global variable 'total' equals to {}.".format(total))



'''
Outputs:

Inside the function, the local variable 'total' equals to 9.
The return value of the function is 9.
The global variable 'total' equals to 9.

'''



