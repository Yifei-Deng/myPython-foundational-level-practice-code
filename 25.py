'''
视频中老师演示的代码
python开发基础25-列表的定义及特性介绍

'''

a = [1,'hello',3.14,print(1),[1,2,3,[3.1,3.2,3.3]],{'name':'whatever'}]
print(type(a))

#print hello
print(a[1])

#print 2
print(a[4][1])

#print 3.3
print((a[4][3][2]))

#slice,print hello
print(a[1:2])

#slice,print 3.1,3.2,3.3
print(a[4][3][:])

#change 3.14 to 3.14159
a[2] = 3.14159
print(a)

#joint two lists
b = [1,2,3,4]
c = a+b
print(c)
c = b+a
print(c)

'''
Example Outputs:

1
<class 'list'>
hello
2
3.3
['hello']
[3.1, 3.2, 3.3]
[1, 'hello', 3.14159, None, [1, 2, 3, [3.1, 3.2, 3.3]], {'name': 'whatever'}]
[1, 'hello', 3.14159, None, [1, 2, 3, [3.1, 3.2, 3.3]], {'name': 'whatever'}, 1, 2, 3, 4]
[1, 2, 3, 4, 1, 'hello', 3.14159, None, [1, 2, 3, [3.1, 3.2, 3.3]], {'name': 'whatever'}]


'''