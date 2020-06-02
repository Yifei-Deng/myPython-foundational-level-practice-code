'''
视频中老师演示的代码
python开发基础17-number数值型

'''

a=10   #定义一个整形（数）
print(a)

f=2.14   #定义一个浮点型（数）
print(f)

print(float(a)+f)  #强制将a从int转换为float


num=input("\nplease enter a number: ")
print(type(num))   #py3中input函数会将输入全部统一以字符串的形式返回
                   #而py2中的input将会根据用户不同的输入类型进行返回值

num=(int(num)+1)      #强制将num从str转换为int


print(str(num)+" days")     #强制将num转换为str

'''
Output:

10
2.14
12.14

please enter a number: 99
<class 'str'>
100 days

'''