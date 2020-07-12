'''

python开发基础58-Python数据库的操作

'''

import pymysql

def data_search():
    '''
    查询数据
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*', database='employeeDB')
    cursor = db.cursor()

    sql = "select * from employees where Department = '%s'" %'First Order'
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        name = row[1]
        age = row[2]
        department = row[4]
        address = row[5]

    print('My name is {}, I am {} years old.\nI work for {}, and I live at {}.'.format(name,age,department,address))
    db.close()

if __name__ == '__main__':
    data_search()


'''
Outputs:

My name is Kylo Ren, I am 32 years old.
I work for First Order, and I live at 123 Snoke Street.


'''
