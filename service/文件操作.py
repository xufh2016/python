# 打开文件 with关键字用于python的上下文管理器机制，它可以保证文件会被正常关闭，不需要再写close语句.with语句仅能用于支持上下文管理歇息的对象
with open("D:\\test01.txt", "r", encoding="utf-8") as f:
    # read()方法不带参数时，是一次性全部读取，大文件时不可使用read不带参数的方式
    a = f.read()
    # print(a)
    for line in a: # 这种方式是一次读取一行
        print(line ,end="")
    # 关闭文件
    num = f.tell()
    print(num)
# f.close()