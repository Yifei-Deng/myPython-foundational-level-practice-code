'''

python开发基础51-面向对象3大特性之封装

'''

class Demo:

    def __init__(self):
        self.__x = 10     #隐藏属性
        self.y = 20       #普通实例属性

    def get_x(self):           #对外访问接口
        return self.__x

    def set_x(self):         #对外设置接口
        x = int(input('Please enter the new value of x:'))

        while x < 10:
            x = int(input('The value of x cannot be less than 10, please enter again:'))

        self.__x = x


if __name__ == '__main__':

    demo = Demo()

    print('x =',demo.get_x())
    Demo.set_x(demo)
    print('x =', demo.get_x())



'''
Sample Outputs:

x = 10
Please enter the new value of x:4
The value of x cannot be less than 10, please enter again:8
The value of x cannot be less than 10, please enter again:2
The value of x cannot be less than 10, please enter again:12
x = 12





'''










