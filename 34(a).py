'''

python开发基础34-if分支判断结构

'''

grade = int(input("Please enter your grade:"))

if 100 >= grade > 89:               #if grade <= 100 and grade > 89
    print("Letter Grade: A")
elif 89 >= grade > 79:              #if grade <= 89 and grade > 79
    print("Letter Grade: B")
elif 79 >= grade > 69:              #if grade <= 79 and grade > 69
    print("Letter Grade: C")
elif 69 >= grade > 59:              #if grade <= 69 and grade > 59
    print("Letter Grade: D")
elif 59 >= grade >= 0:              #if grade <= 59 and grade >= 0
    print("Letter Grade: F")
else:
    print("Invalid Input.")

'''
Example Outputs:

Please enter your grade:80
Letter Grade: B

Please enter your grade:666
Invalid Input.

'''




