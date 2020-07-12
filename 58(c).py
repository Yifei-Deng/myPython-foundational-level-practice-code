'''

python开发基础58-Python数据库的操作

'''

import pymysql

def data_delete():
    '''
    删除数据
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*', database='employeeDB')
    cursor = db.cursor()

    sql = "delete from employees where Name = '%s'" % 'Ben Solo'
    cursor.execute(sql)
    db.commit()
    db.close()

if __name__ == '__main__':
    data_delete()