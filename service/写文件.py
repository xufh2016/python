stream = open("D:/py1.txt", "a")
s = '''
你好鸭
    欢迎来到澳门博彩赌场，赠送给你一个icon
           赌神：高进
           赌侠：周星星
'''
if stream.writable():
    re = stream.write(s)
    print(re)  # 打印了66
    stream.write('''扮演者：周润发''')
stream.close()  # 释放资源
''''
在写（w模式）模式：w表示写操作
写文件时，可以不预先创建文件，在open时候会直接创建
方法：
    write(内容) 每次会将原来的内容清空，然后写当前内容
    
'''