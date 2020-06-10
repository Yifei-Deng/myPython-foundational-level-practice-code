'''
视频中老师演示的代码
python开发基础26-列表的常用方法

'''

a = [1,2,3,4]

#求列表当中最大的值,只适合纯数字列表中的元素比较
print(max(a))

#求列表当中最小的值,只适合纯数字列表中的元素比较
print(min(a))

#如何将字符串转换为列表
astr = 'hello'
alist = list(astr)
print(alist)

#append: 在列表的末尾添加新的元素
a.append('hello')
print(a)

#count:统计某个元素在列表中出现的次数
print(a.count('hello'))

b = [1,2,3,[1,2,5]]
print(a.count(1))  #注意无法用count统计嵌套列表中的元素

#extend：在列表的末尾添加另一个序列中的多个值（用新列表扩充原列表）
a.extend(b)   #extend在原列表a上添加b的新元素；而a+b不会改变2个列表本身的元素，返回的则是一个新列表。
print(a)

#index：从列表中找出某个值第一次出现的索引位置
print(b.index(1))

'''
Outputs:

4
1
['h', 'e', 'l', 'l', 'o']
[1, 2, 3, 4, 'hello']
1
1
[1, 2, 3, 4, 'hello', 1, 2, 3, [1, 2, 5]]
0


'''