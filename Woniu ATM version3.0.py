'''
WoniuATM

a. 在前面项目的基础上进一步改进，要求使用一个二位列表来保存用户名和密码

b. 添加如下操作主菜单，用户选择对应的菜单选项进行操作，每次操作完成后继续进入主菜单，用户输入3之后可以结束并退出应用

   *****************Welcome to Woniu ATM*****************
   ******Please Choose One of The Following Options******
   **************1.Sign Up 2.Log In 3.Exit***************

'''

users = [
    ['Rey','5P1Wsl'],
    ['Rose','pPofPI'],
    ['Finn','FL4J4L']
]

def get_menu():
    menu = '''
    *****************Welcome to Woniu ATM*****************
    ******Please Choose One of The Following Options******
    **************1.Sign Up 2.Log In 3.Exit***************
    '''

    while True:
        print(menu)
        op = input('Please enter your option: ')

        if op == '1':
            reg()
        elif op == '2':
            login()
        elif op == '3':
            print('Thanks for using Woniu ATM, see you next time...')
            break
        else:
            print('Invalid input, please try again!')


def reg():
    print("Welcome to Woniu ATM, sign up now!")

    while True:
        return_flag = True
        user = input('Please enter the username for your new account: ')

        for record in users:
            if record[0] == user:
                print('The username has already been taken, try another!')
                return_flag = False
                break

        if return_flag:
            break

    while True:
        pw = input('Please enter the password for your new account: ')

        if len(pw) < 6:
            print("Your password can't be less then 6 characters long, try another!")
        else:
            users.append([user,pw])
            print('Thanks for signing up with Woniu ATM. Redirecting to the Start menu... ')
            return

def login():
    return_flag = False
    while True:
        user = input('Please enter your username: ')
        pw = input('Please enter your password: ')

        for record in users:
            if record[0] == user and record[1] == pw:
                print('Hello {}!'.format(user))
                return_flag = True
                break

        if return_flag:
            break
        else:
            print('The username or password you entered is incorrect, please try again!')


if __name__ == '__main__':
    get_menu()


'''
Example Outputs:


    *****************Welcome to Woniu ATM*****************
    ******Please Choose One of The Following Options******
    **************1.Sign Up 2.Log In 3.Exit***************
    
Please enter your option: 1
Welcome to Woniu ATM, sign up now!
Please enter the username for your new account: Rey
The username has already been taken, try another!
Please enter the username for your new account: Poe
Please enter the password for your new account: 123
Your password can't be less then 6 characters long, try another!
Please enter the password for your new account: 123456
Thanks for signing up with Woniu ATM. Redirecting to the Start menu... 

    *****************Welcome to Woniu ATM*****************
    ******Please Choose One of The Following Options******
    **************1.Sign Up 2.Log In 3.Exit***************
    
Please enter your option: 2
Please enter your username: Poe
Please enter your password: 123456
Hello Poe!

    *****************Welcome to Woniu ATM*****************
    ******Please Choose One of The Following Options******
    **************1.Sign Up 2.Log In 3.Exit***************
    
Please enter your option: 3
Thanks for using Woniu ATM, see you next time...




'''




