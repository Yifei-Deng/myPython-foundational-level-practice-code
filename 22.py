"""
视频中老师演示的代码
python开发基础22-字符串的切片操作

"""

s = 'Hello,how are you?'

#提取从开头到结尾整个字符串的全部内容
result = s[:]
print(result)

#截取'how are you?'
result = s[6:]
print(result)
result = s[-12:]
print(result)

#截取'Hello'
result = s[:5]
print(result)
result = s[:-13]
print(result)

#截取'how'
result = s[6:9]
print(result)
result = s[-12:-9]
print(result)

#截取标点符号和空格
result = s[5::4]
print(result)

#将字串符反序输出
result = s[::-1]
print(result)

#将'how'反序输出
result = s[8:5:-1]
print(result)


'''
Outputs:

Hello,how are you?
how are you?
how are you?
Hello
Hello
how
how
,  ?
?uoy era woh,olleH
woh

正序输出 [a:b:1], a<b, 左闭右开, 能取到a，但无法取到b
反序输出 [a:b:-1], a>b, 右闭左开, 能取到a，但无法取到b

'''