'''

python开发基础57-Python数据库的操作

'''

import pymysql

def create_db():
    '''
    创建一个新的数据库
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*')
    cursor = db.cursor()

    cursor.execute('create database if not EXISTS employeeDB')             #指定要执行的sql语句
    db.close()

if __name__ == '__main__':
    create_db()


