'''

视频中老师演示的代码
python开发基础30-集合

'''

a = {1,2,3,'hello',(1,2,3)}
print(a)               #无序打印
print(type(a))

# b = [1,2,3]
# 如果定义一个集合: a = {1,2,3,b} 则会报错
# 因为b是一个列表,列表是一种unhashable  variable, 而集合中无法包括unhashable  variable

#添加元素
a.add(4)
print(a)

#print(a[1])=ERROR 集合是无序的，无法用indexing去定义元素

#删除元素
a.remove('hello')
print(a)

#计算长度
print(len(a))

#查找元素
print(1 in a)

#删除集合
a.clear()
print(a)



'''
Example Outputs:

{1, 2, 3, 'hello', (1, 2, 3)}
<class 'set'>
{1, 2, 3, 'hello', 4, (1, 2, 3)}
{1, 2, 3, 4, (1, 2, 3)}
5
True
set()


'''






