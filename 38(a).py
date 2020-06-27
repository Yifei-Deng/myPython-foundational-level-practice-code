'''

python开发基础38-函数的位置、关键字、及默认参数

'''

def fun1(name,age):
    print('My name is {}, and I am {} years old.'.format(name,age))

fun1('Jane',32)                               #'Jane'和25就是用户在调用函数时从外部传入的变量，我们可以在函数中任意使用这些变量来进行操作

fun1(age=25,name='John')                      #调用函数时，通过“键值对”方式来进行传参，可以让函数更加清晰，容易使用，同时也避免了参数的顺序要求

def fun2(name,age,employer='ABC Limited'):    #定义函数时，为参数提供默认值，在调用函数时可传这个参数的值，也可以不传（**所有的位置参数必须出现在默认参数前)
    print('My name is {}, I am {} years old, and I work for {}.'.format(name,age,employer))

fun2('Jane',32)
fun2('John',25)


'''
Outputs:

My name is Jane, and I am 32 years old.
My name is John, and I am 25 years old.
My name is Jane, I am 32 years old, and I work for ABC Limited.
My name is John, I am 25 years old, and I work for ABC Limited.

'''







