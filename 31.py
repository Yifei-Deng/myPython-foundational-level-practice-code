'''

视频中老师演示的代码
python开发基础31-字典的定义&基本特性

'''

#定义一个字典
d1 = {'Name':'John Doe','Address':'123 Main Street','Age':25,'Occupation':'Unemployed'}

print(type(d1))
print(d1)

#访问一个键所对应的值
print(d1['Name'])
print(d1['Address'])

#修改字典中某个键所对应的值
d1['Occupation'] = 'Accountant'

#添加一个键以及其所对应的值
d1['Employer'] = 'ABC Limited'

#删除一个键以及其所对应的值
del d1['Address']

print(d1)

'''
Outputs:

<class 'dict'>
{'Name': 'John Doe', 'Address': '123 Main Street', 'Age': 25, 'Occupation': 'Unemployed'}
John Doe
123 Main Street
{'Name': 'John Doe', 'Age': 25, 'Occupation': 'Accountant', 'Employer': 'ABC Limited'}

'''








