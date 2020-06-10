'''
视频中老师演示的代码
python开发基础27-列表的常用方法

'''

#sort：对列表排序（纯数字）
s = [1,3,4,5,7,8,2]
s.sort()              #从小到大
print(s)

s.sort(reverse=True)  #从大到小
print(s)

s1 = [1,3,"4","5",7,8,2]
s1.sort(key=lambda x:int(x))  #key对于"4"和"5"进行整数处理
print(s1)

#clear：清空列表
s1.clear()
print(s1)



'''
Outputs:

[1, 2, 3, 4, 5, 7, 8]
[8, 7, 5, 4, 3, 2, 1]
[1, 2, 3, '4', '5', 7, 8]
[]


'''