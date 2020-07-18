'''
WoniuATM

a. 在前面项目的基础上进一步改进，要求使用一个列表加字典的形式来保存用户的信息，并增加一个账户余额信息项,
   用户信息的保存格式如下：
   users_list = [{'user':'','password:'','balance':0},{},{}...]

b. 添加如下操作主菜单，用户选择对应的菜单选项进行操作，每次操作完成后继续进入主菜单，用户输入4之后可以结束并退出应用,
   用户注册成功后奖励3000元

   *************************Welcome to Woniu ATM*************************
   **************Please Choose One of The Following Options**************
   **************1.Sign Up 2.Log In 3.Check Balance 4.Exit***************

'''

users_list = [
    {'user':'Rey','password':'5P1Wsl','balance':1500},
    {'user':'Rose','password':'pPofPI','balance':100000},
    {'user': 'Finn', 'password': 'FL4J4L', 'balance': 10120}
]

is_login = False
current_user = None

def get_menu():
    menu = '''
    *************************Welcome to Woniu ATM*************************
    **************Please Choose One of The Following Options**************
    **************1.Sign Up 2.Log In 3.Check Balance 4.Exit***************
    '''

    while True:
        print(menu)
        op = input('Please enter your option: ')

        if op == '1':
            reg()
        elif op == '2':
            login()
        elif op == '3':
            check_balance()
        elif op == '4':
            print('Thanks for using Woniu ATM, see you next time...')
            break
        else:
            print('Invalid input, please try again!')

def reg():
    print("Hello there, let's create your account!")

    while True:
        return_flag = True
        name = input('Please enter the username for your new account: ')

        for record in users_list:
            if record['user'] == name:
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
            users_list.append({'user': name, 'password': pw, 'balance': 3000})
            print('Thanks for signing up with Woniu ATM. You have won a $3000 reward!')
            return


def login():
    return_flag = False

    while True:
        name = input('Please enter your username: ')
        pw = input('Please enter your password: ')

        for record in users_list:
            if record['user'] == name and record['password'] == pw:
                print('Hello {}!'.format(name))
                return_flag = True
                break

        if return_flag:
            global is_login,current_user
            is_login = True
            current_user = name

            break
        else:
            print('The username or password you entered is incorrect, please try again!')


def check_balance():

    #如果要查询余额，首先必须要登录，调用函数前必须检查登录状态，并且要知道当前登录的用户是谁。

    if is_login and current_user:
        for record in users_list:
            if record['user'] == current_user:
                print('Hey {}, you current balance is ${}.'.format(current_user,record['balance']))
                break
    else:
        print('Please log in first to access your account balance!')

if __name__ == '__main__':
    get_menu()





