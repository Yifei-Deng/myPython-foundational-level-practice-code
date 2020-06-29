'''

python开发基础42-匿名函数lambda

'''

fun1 = lambda x,y: x + y   #定义的是单行函数，如果一个函数比较复杂，应该定义为普通函数
print(fun1(1,2))

fun2 = lambda: print('hello')
fun2()

def for_sort(x):
    return list(x.values())[0]

myList1 = [{'English':2},{'Math':1},{'Chinese':3}]
myList1.sort(key=for_sort)
print(myList1)

myList2 = [{'English':83},{'Math':95},{'Chinese':78}]
myList2.sort(key=lambda x:list(x.values())[0],reverse=True)
print(myList2)


'''
Outputs:

3
hello
[{'Math': 1}, {'English': 2}, {'Chinese': 3}]
[{'Math': 95}, {'English': 83}, {'Chinese': 78}]

'''








