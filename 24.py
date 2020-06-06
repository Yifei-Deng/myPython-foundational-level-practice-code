"""
视频中老师演示的代码
python开发基础24-字符串的常用函数

"""

s = "Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus"

#isdigit：判断指定的字符串是否只包含数字
print(s.isdigit())

password = input("请输入数字密码：")
if password.isdigit():
    print("输入正确")
else:print("你输入的不是数字")

#islower: 判断字符串是否包含至少一个区分大小写的字符
print(s.islower())

#lower，upper：将字符串中的字母全部变成小写(lower)或大写(upper)
print(s.upper())
print(s.lower())

#startwith:用作于判断一个字符串是否以指定的子字符串开头
print(s.startswith('Guido'))

#endwith:用作于判断一个字符串是否以指定的子字符串结束
print(s.endswith('circus'))      # s以Circus结束, 所以是False

#strip：删除原字符串中左右两边指定的字符，如果不指定删除的字符，则默认删除左右两边的空白字符
s = "引用自百度百科Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus引用自百度百科"
print(s.strip('引用自百度百科'))

#lstrip,rstrip: 删除原字符串中左边(lstrip)或右边(rstrip)指定的字符
print(s.lstrip('引用自百度百科'))
print(s.rstrip('引用自百度百科'))

'''
Example Outputs:

False
请输入数字密码：123
输入正确
False
GUIDO VAN ROSSUM 之所以选中 PYTHON (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 MONTY PYTHON'S FLYING CIRCUS
guido van rossum 之所以选中 python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 monty python's flying circus
True
False
Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus
Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus引用自百度百科
引用自百度百科Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus


'''

