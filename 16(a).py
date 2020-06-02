'''
视频中老师演示的代码
python开发基础16-format格式化函数

'''
#按顺序的格式化输出
print("{} and {}" .format('Ben','Jerry'))   #用{  } 作为占位符，代替了%s

#不按顺序，指定输出的数据的位置
print("When {1} met {0}" .format('Sally','Harry'))  #顺序从0开始

#键值对方式指定数据
print("The website is {web}, and the URL is {url}".format(web='Google',url='http://google.com'))

print("{:.2f}".format(3.1415927))     #对浮点数的格式化，用:代替了%
print("{:.0f}".format(3.1415927))     #不显示小数点后面的数字

print("我今年{}岁。".format(25))    #用{  } 作为占位符，代替了%d

'''
output:

Ben and Jerry                                                                                                           
When Harry met Sally                                                                                                    
The website is Google, and the URL is http://google.com                                                                 
3.14                                                                                                                    
3                                                                                                                       
我今年25岁。


'''