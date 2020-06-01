'''

视频中老师演示的代码
python开发基础12-python2 & 3的主要区别 8分25秒
python 3的例子

'''
a=10
b=20
c="hello"

print(a,b,c,sep="#",end="")
print("end")

#output: 10#20#helloend 

#在python 3中print是函数，sep和end是参数
#sep能用来添加分隔符（separators），所以在a与b,和b与c之间的空格由#代替
#原本 end 默认为 ‘\n', 即为开始新的一行