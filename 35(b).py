'''

python开发基础34-for&while循环结构

'''

a = [1,2,3,4,5]

print('Break Statement:')
for item in a:
    if item == 4:
        break         # jump out of the loop
    print(item,end=' ')

print('\nContinue Statement:')
for item in a:
    if item == 4:
        continue      # skip if a specified condition occurs
    print(item,end=' ')

'''
Outputs:

Break Statement:
1 2 3 
Continue Statement:
1 2 3 5 

'''



