'''

python开发基础58-Python数据库的操作

'''

import pymysql

def data_update():
    '''
    更新数据
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*', database='employeeDB')
    cursor = db.cursor()

    sql = "update employees set Name = '%s' where ID = %s" %('Ben Solo',1)
    cursor.execute(sql)
    db.commit()
    db.close()

if __name__ == '__main__':
    data_update()