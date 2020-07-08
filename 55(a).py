'''

python开发基础54-Python文件写入

'''

with open(r'/Users/Yifei/Desktop/py3/53~/file/test.txt',mode='r+',encoding='utf8') as f:


    f.write('I want to add this new line.\n')


    f.writelines([
        'Success is not final, failure is not fatal;\n',
        'It is the courage to continue that counts.\n',
        '                      ---Winston Churchill\n'
    ])








