'''

python开发基础35-for&while循环结构

'''

names = ['张三','李四','王五']

for name in names:
    if name == '张三':
        print('找到了{}。'.format(name))
        break
else:
    print('没有找到张三。')

'''
Outputs:

找到了张三。

'''