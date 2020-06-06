'''
视频中老师演示的代码
python开发基础20-random模块的使用

'''

import random               #import the module 

#返回[0.0, 1.0)之间的浮点数。[0.0, 1.0)是左闭右开的区间，能取到0.0，但无法取到1.0
result=random.random()
print(result)

##生成一个a与b之间的随机整数, [a,b)是左闭右开的区间，能取到a，但无法取到b
result=random.randrange(5,10)
print(result)


#生成一个a与b之间的随机整数, [a,b]是左右闭合的区间，既能够取到a，也可以取到b
result=random.randint(5,10)
print(result)

#生成[a,b]之间随机的浮点数
result=random.uniform(5,10)
print(result)

#从列表中随机选择一个数
result=random.choice([5,6,7,8,9,10])
print(result)

#洗牌，打乱列表中元素的顺序
myArray=[5,6,7,8,9,10]
result=random.choice(myArray)
print(myArray)

#从列表中随机取出n个元素
result=random.sample(myArray,3)
print(result)



'''
Eample Outputs:

0.6170906902597835                                                                                                      
7                                                                                                                       
5                                                                                                                       
5.649804621852119                                                                                                       
9                                                                                                                       
[5, 6, 7, 8, 9, 10]                                                                                                     
[7, 10, 8]



'''