'''
视频中老师演示的代码
python开发基础21-string的定义和使用

'''

#用单引号定义字符串
s='what is this?'
print(type(s))

#用双引号定义字符串
s="what's this?"
print(type(s))

#当字符串的内容本身有单引号或双引号时，外面的引号必须跟包含的引号格式不同
s='she asked "what is this?"'
print(s)

#用三引号定义字符串,用作于大段文本的定义、语句的注释或函数注释
'''
Outputs:

<class 'str'>                                                                                                           
<class 'str'>                                                                                                           
she asked "what is this?"

'''