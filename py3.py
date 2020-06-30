'''

python开发基础43-包和模块

'''

#通过from...import...选择性导入指定的资源
from py1 import a
from py1 import fun1
from py1 import *            # *导入所有资源

print(a)
fun1('World')        #避免每次在调用其他模块的变量或函数时，每次都输入包名或模块名



'''
Outputs:

1
Hello World


'''




