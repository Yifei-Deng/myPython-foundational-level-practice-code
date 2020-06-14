'''

python开发基础32-字典的常用方法

'''

d1 = {'Name':'John Doe','Age':25,'Occupation':'Unemployed','Birthday':[1995,5,25]}

# 求字典的长度
print(len(d1))

# 清空字典
# d1.clear()
# print(d1)

print('浅拷贝:')
d2 = d1
d2['Name'] = 'John Smith'
print('d1字典为',d1)
print('d2字典为',d2)

print('深拷贝:')
d2 = d1.copy()
d1['Name'] = 'John Doe'
d1['Birthday'].reverse()       #如果字典中某个键的值为列表，该键将仍然是浅拷贝
print('d1字典为',d1)
print('d2字典为',d2)

'''
Outputs:

4
浅拷贝:
d1字典为 {'Name': 'John Smith', 'Age': 25, 'Occupation': 'Unemployed', 'Birthday': [1995, 5, 25]}
d2字典为 {'Name': 'John Smith', 'Age': 25, 'Occupation': 'Unemployed', 'Birthday': [1995, 5, 25]}
深拷贝:
d1字典为 {'Name': 'John Doe', 'Age': 25, 'Occupation': 'Unemployed', 'Birthday': [25, 5, 1995]}
d2字典为 {'Name': 'John Smith', 'Age': 25, 'Occupation': 'Unemployed', 'Birthday': [25, 5, 1995]}

'''


