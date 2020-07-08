'''

python开发基础54-Python文件写入

'''


# 以二进制模式写入字节串，一般我们保存图片、音视频等二进制文件时需要用write方法来写入



import requests
resp = requests.get('https://i.pinimg.com/originals/d1/22/32/d12232a8ec1f06cd3fd611761fa6a88c.jpg')
with open('winston.jpg',mode='wb') as f:
    f.write(resp.content)





