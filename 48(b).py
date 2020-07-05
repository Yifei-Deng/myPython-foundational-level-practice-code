'''

python开发基础48-类的方法和属性

'''


class Students:

    def __init__(self,name,age,studentID):
        self.n = name
        self.a = age
        self.i = studentID

    def study(self):
        print('I am studying Python')

class inheritStudents(Students):

    def school(self):
        print('I am a student at ABC school')

if __name__ == '__main__':
    student = inheritStudents('Jane Johnson',35,'M111')
    print('My name is {}, and I am {} years old'.format(student.n,student.a))
    student.school()
    student.study()
    print('My student number is', student.i)


'''
Outputs:


My name is Jane Johnson, and I am 35 years old
I am a student at ABC school
I am studying Python
My student number is M111




'''




