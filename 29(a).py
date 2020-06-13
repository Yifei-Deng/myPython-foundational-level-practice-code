'''

视频中老师演示的代码
python开发基础29-元组

'''

a = (2,4,6)      #define a tuple

print(type(a))
print(len(a))
print(max(a))
print(min(a))

b = ['2.1','2.2','2.3']
c = (1,2,b)

b.append('2.4')       #只可以修改元组内嵌套的列表的元素
print(c)

d = (1)               #只有一个元素的元组并不是元组；而是根据括号内元素的类型来决定其性质
print(type(d))
d = (1,)              #在元素后加一个逗号也可以定义一个只有一个元素的元组
print(type(d))


'''
Outputs:

<class 'tuple'>
3
6
2
(1, 2, ['2.1', '2.2', '2.3', '2.4'])
<class 'int'>
<class 'tuple'>


'''