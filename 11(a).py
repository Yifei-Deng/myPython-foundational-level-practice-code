'''

视频中老师演示的代码
python开发基础11-python基本特性介绍 10分50秒

'''
arr=[15,34,56,67,32,22,11]

arr.sort()

print(arr)

#output: [11, 15, 22, 32, 34, 56, 67]

#下面的代码也会产出同样的output：

#arr=[15,34,56,67,32,22,11]

#for i in range(len(arr)):
#    for j in range(0,len(arr)-i-1):
#       if arr[j]>arr[j+1]:
#            arr[j],arr[j+1]=arr[j+1],arr[j]
            
#print(arr)