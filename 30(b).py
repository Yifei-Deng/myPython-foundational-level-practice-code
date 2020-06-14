'''

视频中老师演示的代码
python开发基础30-集合

'''

#强制转换
print(set('hello'))       #会把其中的一个'l'去掉
print(set([1,2,1]))       #把列表转换为集合；去掉重复的1

#数学操作
a = {1,2,3}
b = {3,4,5}

print(a | b)      #并集
print(a & b)      #交集
print(a - b)      #差集
print(a ^ b)      #对称差集


'''
Example Outputs:

{'o', 'l', 'h', 'e'}
{1, 2}
{1, 2, 3, 4, 5}
{3}
{1, 2}
{1, 2, 4, 5}

'''