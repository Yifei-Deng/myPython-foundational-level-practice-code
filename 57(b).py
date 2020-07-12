'''

python开发基础57-Python数据库的操作

'''

import pymysql

def create_table():
    '''
    创建一张表
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*',database='employeeDB')
    cursor = db.cursor()

    cursor.execute('drop table if EXISTS employees')             #指定要执行的sql语句
    sql = '''
          create table employees(
                 ID int PRIMARY KEY,
                 Name char(20) not null,
                 Age int,
                 Gender char(1),
                 Department char(20) not null,
                 Address char(40) not null
           )
    '''

    cursor.execute(sql)
    db.close()

if __name__ == '__main__':
    create_table()



