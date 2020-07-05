'''

python开发基础51-面向对象3大特性之封装

'''



class Demo:

    def __init__(self):
        self.__x = 10  # 隐藏属性
        self.y = 20  # 普通实例属性

    def __hideHello(self):
        print('Hello')

    def getHello(self):
        self.__hideHello()

if __name__ == '__main__':

    demo = Demo()
    demo.getHello()

'''
Output:

Hello



'''





