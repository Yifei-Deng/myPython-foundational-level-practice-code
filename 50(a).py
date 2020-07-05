'''

python开发基础50-子类的初始化方法

'''

class Students:

    def __init__(self,name,age,studentID):
        self.n = name
        self.a = age
        self.i = studentID

    def study(self):
        print('I am studying Python')

class inheritStudents(Students):

    def __init__(self,name,age,studentID,address):
        Students.__init__(self,name,age,studentID)   #显示调用父类的初始化方法，使父类能够被正确的初始化
        self.address = address          #添加新的属性

    def school(self):
        print('I am a student at ABC school')

    def study(self):
        print('I am studying astrology')   #如果在子类中定义了跟父类同名的方法，则子类的方法将覆盖父类的这个方法，实现子类方法的自定义

if __name__ == '__main__':
    student = inheritStudents('Jane Johnson',35,'M111','123 Main Street')
    print('My name is {}, and I am {} years old'.format(student.n,student.a))
    student.school()
    student.study()
    print('My student number is {}, and I live at {}'.format(student.i,student.address))

'''
Outputs:

My name is Jane Johnson, and I am 35 years old
I am a student at ABC school
I am studying astrology
My student number is M111, and I live at 123 Main Street





'''





