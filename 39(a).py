'''

python开发基础39-可变参数

'''

# *args:一个元组类型的参数，在函数调用时，所有的位置参数将进入到args这个元组中
# **kwargs：一个字典类型的参数，在函数调用时，所有的关键字参数将进入到kwargs这个字典中
def fun1(*args,**kwargs):
    print("The arguments are {}, and there're {} arguments.".format(type(args),len(args)))
    for i in args:
        print(i)

    print("The keyword arguments are {}, and there're {} keyword arguments.".format(type(kwargs),len(kwargs)))
    for k,v in kwargs.items():
        print(k,v)

fun1(1995,5,25,Name='John Doe',Address='123 Main Street',Occupation='Unemployed')

'''
Outputs:

The arguments are <class 'tuple'>, and there're 3 arguments.
1995
5
25
The keyword arguments are <class 'dict'>, and there're 3 keyword arguments.
Name John Doe
Address 123 Main Street
Occupation Unemployed

'''










