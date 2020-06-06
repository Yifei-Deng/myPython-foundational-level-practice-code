'''
视频中老师演示的代码
python开发基础21-string的定义和使用

'''

#通过len()获取字符串长度
s="it is a dog"
print(len(s))      

#使用\n换行
s='she asked "what is this?"\nhe said "it is a dog"'   
print(s)

#如何打\n等印转义字符
s='she asked "what is this?"\\nhe said "it is a dog"'   
print(s)

#在字符串前面加上r这个字符，就会将该字符串内的所有的转义符变成普通的字符
s=r'she asked "what is this?"\nhe said "it is a dog"'   
print(s)

#在字符串前面加上r这个字符，方便我们打印windows中的路径
path=r"c:\windows\users\notebook"
print(path)



'''
Outputs:

11                                                                                                                      
she asked "what is this?"                                                                                               
he said "it is a dog"                                                                                                   
she asked "what is this?"\nhe said "it is a dog"                                                                        
she asked "what is this?"\nhe said "it is a dog"                                                                        
c:\windows\users\notebook


'''
