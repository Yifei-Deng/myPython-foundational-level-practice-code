'''

python开发基础33-字典的常用方法

'''

d1 = {'Name':'John Doe','Address':'123 Main Street','Occupation':'Unemployed','Age':25}


# setdefault: 跟get方法类似，可以根据指定的键去取对应的值，如果键不存在的话，会添加新键到字典中并将值设为指定的默认值
d1.setdefault('Birthday',[1995,5,25])   #新键如果不指定值，将默认为None
print(d1)

# update: 将原字典用指定的新字典进行更新
d2 = {'Occupation':'Accountant','Employer':'ABC Limited'}    # 如果新字典中的键跟原字典中的键重名，则用新字典中的键的值更新原字典中键的值
d1.update(d2)                                                # 如果新字典中的键不在原字典中，则会新增该键值对到原字典中
print(d1)

# pop:根据指定的键去删除字典中的键值对
print(d1.pop('ID','Not Found'))          #指定一个默认值来避免报错
print(d1.pop('Address','Not Found'))
print(d1)

# popitem: 随机返回并删除字典中的一个键值对（一般都是从末尾开始删）
while len(d1) > 0:     #利用循环来删除字典内所有的键值对
    d1.popitem()
print(d1)

'''
Outputs:

{'Name': 'John Doe', 'Address': '123 Main Street', 'Occupation': 'Unemployed', 'Age': 25, 'Birthday': [1995, 5, 25]}
{'Name': 'John Doe', 'Address': '123 Main Street', 'Occupation': 'Accountant', 'Age': 25, 'Birthday': [1995, 5, 25], 'Employer': 'ABC Limited'}
Not Found
123 Main Street
{'Name': 'John Doe', 'Occupation': 'Accountant', 'Age': 25, 'Birthday': [1995, 5, 25], 'Employer': 'ABC Limited'}
{}

'''

