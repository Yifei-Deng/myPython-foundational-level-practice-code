# coding: utf-8
'''

视频中老师演示的代码
python开发基础12-python2 & 3的主要区别 13分55秒
python 2的例子

'''

a=input("请输入一个值：")

print type(a)
print a+1

#example outputs

#请输入一个值：3
#<type 'int'>
#4

#请输入一个值：s
#ERROR
#ERROR

#请输入一个值：'s'
#<type 'str'>
#ERROR

#py2中的input将会根据用户不同的输入类型进行返回值，输入数字则返回数字，如果要输入字符串则必须要加引号