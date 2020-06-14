'''

python开发基础33-字典的常用方法

'''

d1 = {'Name':'John Doe','Address':'123 Main Street','Age':25,'Occupation':'Unemployed'}

print('keys：取出字典中所有的键')
for key in d1.keys():
    print(key)

print('\nvalues: 取出字典中所有的值')
for value in d1.values():
    print(value)

'''
Outputs:

keys：取出字典中所有的键
Name
Address
Age
Occupation

values: 取出字典中所有的值
John Doe
123 Main Street
25
Unemployed

'''
