'''

python开发基础37-函数的调用

'''

def myFunc():         #调用函数前，必须保证该函数已被定义，否则会报错
    print("hello world")

print(myFunc)         #打印保存该函数的内存地址


myFunc()              #调用该函数，函数调用时必须要添加一个（）

'''
Example Outputs:

<function myFunc at 0x7f8deadb9160>
hello world



'''


