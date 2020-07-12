'''

python开发基础57-Python数据库的操作

'''

import pymysql

def insert_db():
    '''
    插入数据
    :return: none
    '''

    db = pymysql.connect(host='localhost', user='root', password='*IloveJuno*', database='employeeDB')
    cursor = db.cursor()

    sql = "insert into employees(ID,Name,Age,Gender,Department,Address)"\
          "values(%s,'%s',%s,'%s','%s','%s')" %(1, "Kylo Ren",32,'M','First Order','123 Snoke Street')

    effect_rows = cursor.execute(sql)
    db.commit()   #提交数据
    print('The number of rows effected are {}'.format(effect_rows))
    db.close()

if __name__ == '__main__':
    insert_db()

'''
Outputs:

The number of rows effected are 1




'''


