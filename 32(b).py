'''

python开发基础32-字典的常用方法

'''

d1 = {'Name':'John Doe','Address':'123 Main Street','Age':25,'Occupation':'Unemployed'}

# 快速转换一个列表为字典的方法！
# fromkeys: 创建一个新的字典，以序列中元素做为字典的键,可以指定一个val作为字典的值
alist = ['Name','Age','Address','Occupation']
d2 = dict.fromkeys(alist,'NULL')    #如果没有指定val，则默认值为None
print(d2)

# get: 返回指定键的值，如果键不在字典中则返回默认值（默认值可以由我们自己指定）
# print(d1['Employer']) ------>  键不存在会报异常
print(d1.get('Employer', 'default'))
print(d1.get('Name', 'default'))

# in: 判断键是否在字典中，或对字典进行循环
print('Employer' in d1)

# items: 取出字典中以元组形式取出所有的键值对
for item in d1.items():
    print(item[0],':',item[1])

'''
Outputs:

{'Name': 'NULL', 'Age': 'NULL', 'Address': 'NULL', 'Occupation': 'NULL'}
default
John Doe
False
Name : John Doe
Address : 123 Main Street
Age : 25
Occupation : Unemployed

'''







