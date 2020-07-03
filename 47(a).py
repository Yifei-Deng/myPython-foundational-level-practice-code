'''

python开发基础47-类的方法和属性

'''

# 类方法在定义时必须以@classmethod装饰器进行装饰
# 所有的类方法的第一个参数必须是cls
# 类方法不能访问实例属性，只能访问类属性(i.e name)

class Students:

    name = 'John Doe'

    @classmethod
    def printName(cls):
# By using the class method, the function printName takes a single parameter cls, and not self as we usually take.
# cls accepts the class Students as a parameter rather than a single objective.
# Therefore, we can use the class variable age inside the function.

        print('Using class method')
        print('My name is',cls.name)

if __name__ == '__main__':

    Students.printName()


'''
Outputs:

Using class method
My name is John Doe



'''

