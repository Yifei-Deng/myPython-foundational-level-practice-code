'''

视频中老师演示的代码
python开发基础02-程序的定义及构成 11分10秒

'''
arr=[15,34,56,67,32,22,11]

for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)

#output: [11, 15, 22, 32, 34, 56, 67] 
#语法：变量的定义，循环结构，判断结构，比较运算符，赋值运算符
#算法：如何对数组里面的数字进行冒泡，每一次的比较方法，怎么样交换两个数字的值