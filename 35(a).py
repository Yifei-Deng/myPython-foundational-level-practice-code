'''

python开发基础35-for&while循环结构

'''

#当已知循环次数，或者需要在一个集合中进行循环，比如在一个字符串、列表、元组或字典等，最好是使用for循环
for item in [1, 2, 3, 4, 5]:
    print((item + 1))

#当循环次数不一定，只是满足某个条件时需要进行循环时，最好是使用while循环
n = 5
while n > 0:
    print('hello')
    n = n - 1

'''
Outputs:

2
3
4
5
6
hello
hello
hello
hello
hello

'''
