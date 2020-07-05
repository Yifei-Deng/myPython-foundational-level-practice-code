'''

python开发基础48-类的方法和属性

'''

class Students:

    name = 'John Doe'


    @staticmethod
    def printName():
        print('Using static method')
        print('My name is',Students.name)

if __name__ == '__main__':

    Students.printName()

'''
Outputs:

Using class method
My name is John Doe




'''




