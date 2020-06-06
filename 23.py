"""
视频中老师演示的代码
python开发基础23-字符串的常用函数

"""

s = "Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus"

#求字符串的长度
print(len(s))

#count:统计指定的字符或字符串在原字符串中出现的次数
print(s.count('Python'))

#capitalize：将首字母大写
print('hello'.capitalize())

#find: 查找指定的子字符串是否出现在原字符串中，如果出现，则返回第一次出现的索引值。如果不出现，则返回-1
print(s.find('大蟒蛇'))

#replace：将原字符串中的内容替换为指定的内容
print(s.replace('Python','Nohtyp'))
print(s.replace('Python','Nohtyp',1))       #指定替换的次数

#split: 以指定的字符拆分原字符串
print(s.split('，'))

#index:跟find类似，也是查找指定的子字符串是否出现在原字符串中，如果出现，则返回第一次出现的索引值，如果不出现，会抛出异常。
print(s.index('Monty'))


'''
Outputs:

98
2
Hello
31
Guido van Rossum 之所以选中 Nohtyp (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Nohtyp's Flying Circus
Guido van Rossum 之所以选中 Nohtyp (大蟒蛇的意思）作为该编程语言的名字，是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus
['Guido van Rossum 之所以选中 Python (大蟒蛇的意思）作为该编程语言的名字', "是取自英国20世纪70年代首播的电视喜剧 Monty Python's Flying Circus"]
70


'''