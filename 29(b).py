'''

视频中老师演示的代码
python开发基础29-元组

'''

#元组的切片操作
a = (1,2,3,4,5,6,7)
print(a[1:6])

#强制类型转换
b = ['@','!','#']       #list to tuple
c = tuple(b)
print(c)
print(type(c))

print(tuple('okay'))    #string to tuple


'''
Outputs:

(2, 3, 4, 5, 6)
('@', '!', '#')
<class 'tuple'>
('o', 'k', 'a', 'y')

'''