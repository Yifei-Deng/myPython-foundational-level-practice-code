'''
WoniuATM

a.利用2个列表：一个存放用户名；一个存放密码，下标位置一一对应好，
  注册时，要判断 1）用户名是否已经存在；2）密码长度是否大于6位，
  如果输入错误要有相应的提示，并退出系统。

b.如果用户注册成功，则提示用户进行登录，要求用户输入用户名和密码，
  只有当用户名和密码均正确才能提示用户登录成功；
  否则提示用户名或密码错误，并退出系统。

'''

username = ['Rey','Rose','Poe']
password = ['5P1Wsl','pPofPI','sQyRkW']

def reg():

    print("Welcome to Woniu ATM system, sign up now!")
    user = input('Please enter the username for your new account: ')

    if user in username:
        print('The username has already been taken!')
        return False
    else:
        pw = input('Please enter the password for your new account: ')

        if len(pw) < 6:
            print("Your password can't be less then 6 characters long.")
            return False
        else:
            username.append(user)
            password.append(pw)
            print('Thanks for signing up with Woniu ATM. Redirecting to the login page... ')
            return True

def login():
    user = input('Please enter your username: ')
    pw = input('Please enter your password: ')

    if user in username:
        i = username.index(user)
        if password[i] == pw:
            print('Hello {}, welcome back to Woniu ATM!'.format(user))
        else:
            print('The username or password you entered is incorrect.')
    else:
        print('The username does not exist.')


if __name__ == '__main__':

    if reg():
        login()



'''
Example Outputs:

Welcome to Woniu ATM system, sign up now!
Please enter the username for your new account: Finn
Please enter the password for your new account: 123456
Thanks for signing up with Woniu ATM. Redirecting to the login page... 
Please enter your username: Finn
Please enter your password: 123456
Hello Finn, welcome back to Woniu ATM!



'''




