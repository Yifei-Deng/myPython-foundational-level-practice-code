'''
WoniuATM

在v1.0的基础上加入错误重试功能，不管是注册阶段还是登录阶段，
一旦用户输入错误，都将提示用户重新输入，直到用户输入正确或者用户输入'EXIT'为止。

'''

username = ['Rey','Rose','Poe']
password = ['5P1Wsl','pPofPI','sQyRkW']

def reg():
    print("Welcome to Woniu ATM, sign up now!")

    while True:
        user = input('Please enter the username for your new account: ')

        if user == 'EXIT':
            print('Thanks for using Woniu ATM, see you next time...')
            return False

        elif user in username:
            print('The username has already been taken, try another!')

        else:
            while True:
                pw = input('Please enter the password for your new account: ')

                if pw == 'EXIT':
                    print('Thanks for using Woniu ATM, see you next time...')
                    return False

                elif len(pw) < 6:
                    print("Your password can't be less then 6 characters long, try another!")

                else:
                    username.append(user)
                    password.append(pw)
                    print('Thanks for signing up with Woniu ATM. Redirecting to the login page... ')
                    return True



def login():
    while True:
        user = input('Please enter your username: ')
        pw = input('Please enter your password: ')
        if user == 'EXIT' or pw == 'EXIT':
            print('Thanks for using Woniu ATM, see you next time...')
            break
        elif user in username:
            i = username.index(user)
            if password[i] == pw:
                print('Hello {}, welcome back to Woniu ATM!'.format(user))
                break
            else:
                print('The username or password you entered is incorrect.')
        else:
            print('The username or password you entered is incorrect.')

if __name__ == '__main__':

    if reg():
        login()




'''
Example Outputs:

Welcome to Woniu ATM, sign up now!
Please enter the username for your new account: Rey
The username has already been taken, try another!
Please enter the username for your new account: Finn
Please enter the password for your new account: 123
Your password can't be less then 6 characters long, try another!
Please enter the password for your new account: 123456
Thanks for signing up with Woniu ATM. Redirecting to the login page... 
Please enter your username: Finn
Please enter your password: 123456
Hello Finn, welcome back to Woniu ATM!





'''


















