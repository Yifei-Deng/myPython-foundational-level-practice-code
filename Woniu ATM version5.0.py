'''
WoniuATM

a. 添加如下操作主菜单，实现增加的菜单功能。存取款要求只能是100的整数倍。

   ************************* Welcome to Woniu ATM *************************
   ************** Please Choose One of The Following Options **************
   ****************** 1.Sign Up 2.Log In 3.Check Balance ******************
   *************** 4.Deposit 5.Get Cash 6.Transfer 7.Exit *****************

'''

users_list = [
    {'user':'Rey','password':'5P1Wsl','balance':1500},
    {'user':'Rose','password':'pPofPI','balance':100000},
    {'user': 'Finn', 'password': 'FL4J4L', 'balance': 10120}
]

current_user = None

def get_menu():
    menu = '''
    ************************** Welcome to Woniu ATM **************************
    *************** Please Choose One of The Following Options ***************
    ******************* 1.Sign Up 2.Log In 3.Check Balance *******************
    *************** 4.Deposit 5.Withdrawal 6.Transfer 7.Exit *****************
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
            deposit()
        elif op == '5':
            withdrawal()
        elif op == '6':
            transfer()
        elif op == '7':
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

                global current_user
                current_user = record
                print('Hello {}!'.format(current_user['user']))

                return_flag = True
                break

        if return_flag:
            break
        else:
            print('The username or password you entered is incorrect, please try again!')

def check_balance():
    if current_user:
        print('Hey {}, you current balance is ${}.'.format(current_user['user'], current_user['balance']))
    else:
        print('Please login first to access your account balance!')

def deposit():
    if current_user:
        amount = input('Please enter the amount of money you would like to deposit: ')
        if amount.isdigit() and int(amount) % 100 == 0:
            current_user['balance'] += int(amount)
            print('You made a successful deposit, the current balance is $',current_user['balance'])
        else:
            print('Invalid input, please try again!')
    else:
        print('Please login first to access your account!')

def withdrawal():
    if current_user:
        amount = input('Please enter the amount of money you would like to withdrawal: ')
        if amount.isdigit() and int(amount) % 100 == 0 and int(amount) <= current_user['balance']:
            current_user['balance'] -= int(amount)
            print('Withdrawal successful, your current balance is $',current_user['balance'])
        else:
            print('Invalid input, please try again!')
    else:
        print('Please login first to access your account!')

def transfer():
    if current_user:
        receiver = input('Please enter the username of the receiver: ')

        if receiver == current_user['user']:
            print('You cannot transfer money to your own account.')
        else:
            for record in users_list:

                if receiver == record['user']:
                    amount = input('Please enter the amount of money you would like to transfer: ')
                    if amount.isdigit() and int(amount) <= current_user['balance']:
                        current_user['balance'] -= int(amount)
                        record['balance'] += int(amount)
                        print('Successful! The transfer of ${} has been made to {}.'.format(amount,receiver))
                        return
                    else:
                        print('Invalid input, please try again!')
                        return

            print('Sorry, we cannot find the user in our system. Please check again.')
    else:
        print('Please login first to access your account!')


if __name__ == '__main__':
    get_menu()
