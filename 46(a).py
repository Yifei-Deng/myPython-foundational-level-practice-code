'''

python开发基础46-面向对象基本概念

'''

class Students:
    def __init__(self,name,age,studentID):
        self.n = name
        self.a = age
        self.i = studentID

    def study(self):
        print('I am studying Python')


if __name__ == '__main__':
    student = Students('John Doe',25,'A007')
    print(type(student))
    print('My name is',student.n)
    print('I am {} years old'.format(student.a))
    student.study()
    print('My student number is',student.i)


'''
Outputs:

<class '__main__.Students'>
My name is John Doe
I am 25 years old
I am studying Python
My student number is A007



'''














