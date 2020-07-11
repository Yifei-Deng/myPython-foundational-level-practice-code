'''

python开发基础56-Python数据库的操作

'''

import pymysql

def connect_db():
    '''

    通过pymysql连接数据库
    :return: none
    '''

    db = pymysql.connect(host='localhost',user='root',password='*IloveJuno*')
    cursor = db.cursor()

    cursor.execute('select version()')             #指定要执行的sql语句
    data = cursor.fetchone()
    print('数据库版本为：{}'.format(data))

    db.close()

if __name__ == '__main__':
    connect_db()

'''
Output:

数据库版本为：('8.0.20',)



'''

