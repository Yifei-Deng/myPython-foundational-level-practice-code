'''
视频中老师演示的代码
python开发基础19-math模块的使用

'''

import math               #import the module 

print(math.ceil(3.15))   #天花板，取大于3.15的最小的整数值
print(math.ceil(-3.15))   #天花板，取大于-3.15的最小的整数值


print(math.floor(3.15))  #地板，取小于3.15的最大的整数值
print(math.floor(-3.15))  #地板，取小于-3.15的最大的整数值


print(math.ceil(5),math.floor(5))  #如果变量是一个整数，则返回其本身

print(math.fabs(-10))    #取变量的绝对值，返回的是一个浮点数

print(math.fsum([1,2,3,4]))   #对列表里面的每个元素求和，返回的是浮点数

print(math.pow(8,2))        # 8**2等价，返回的是浮点数

print(math.sqrt(64))       #对64开方，返回的是浮点数，

a=(math.sqrt(5))
print("%.2f" %a)           #可以通过 %.xf 来改变能显示的小数点后的数位
print("{:.2f}".format(a))  #可也以通过.format 来改变能显示的小数点后的数位


'''
Output:

4 
-3 
3 
-4 
5 5 
10.0 
10.0 
64.0 
8.0 
2.24 
2.24

'''

