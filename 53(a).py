'''

python开发基础53-Python文件读取

'''

f = open('/Users/Yifei/Desktop/py3/53~/file/test.txt')

while True:
    ch = f.read(1)

    if not ch:
        break

    print(ch,end='')


f.close()


'''
Outputs:

Congratulations!
You have opened it successfully!




'''



