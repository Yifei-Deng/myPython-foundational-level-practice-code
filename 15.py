'''
视频中老师演示的代码
python开发基础15-占位符的使用

'''
#%d的使用

age=25.5
print("我今年%d岁。" %(25))
print("我今年%d岁。" %(age))       #显示整数
print("我今年%10d岁。\n" %(age))     #指定占位宽度

#%s的使用

name="李四"
print("我叫%s。" %("李四"))
print("我叫%s。" %(name))
print("我叫%10s。\n" %(name))    #指定占位宽度

#%f的使用

num=123.456
print("我的存款有%.2f元。" %(123.456))
print("我的存款有%f元。" %(num))       #若不做特殊指定，浮点数会默认显示小数点后6位
print("我的存款有%10.2f元。\n" %(num))   #指定占位宽度

print("我叫%s，我今年%d岁，我的存款有%.2f元。" %(name,age,num))
#通过指定键的方式，对应起来提供值
print("我叫%(name)s，我今年%(age)d岁，我的存款有%(num).2f元。\n" %{"name":"张三","age":20,"num":654.321})

#如何打印百分号
print("水果的水分占总重量的%d%%。" %(15))   #需要在要打印的%前面再写一个%

'''
output:

我今年25岁。                                                                                                            
我今年25岁。                                                                                                            
我今年        25岁。                                                                                                    
                                                                                                                        
我叫李四。                                                                                                              
我叫李四。                                                                                                              
我叫        李四。                                                                                                      
                                                                                                                        
我的存款有123.46元。                                                                                                    
我的存款有123.456000元。                                                                                                
我的存款有    123.46元。                                                                                                
                                                                                                                        
我叫李四，我今年25岁，我的存款有123.46元。                                                                              
我叫张三，我今年20岁，我的存款有654.32元。                                                                              
                                                                                                                        
水果的水分占总重量的15%。

'''