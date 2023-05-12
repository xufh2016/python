print("please input your name")
name = input()
print("your name is ", name)
print("please input your age")
# 通过input函数输入的都是字符串，要转数字需要使用eval函数
age = eval(input())
print("your age is ", age)
# 注释
if age > 40:
    print(age > 40)
    print("~~~~~~~~~~~~~")
else:
    print("---------------------")
#  注意r''转义的用法
print(r'asfd///////sdfs"///////')
content = '''
青青子衿，悠悠我心。

纵我不往，子宁不嗣音？'''
print(content)
print(type("222"))
"""注释
1. 布尔值，布尔值和布尔代数的表示完全一致，只有True、False两种值（注意大小写）
2. 布尔值可以用and、or和not运算
"""
"""
python中的常量：就是不能变的变量，通常使用全部大写的方式表示常量变量名
关于除法：
1. / 计算结果是浮点数，即便能整除，后面也会小数点后加零的形式
2. // 地板除，不管能不能除尽，也去整数,地板除不存在四舍五入，全是舍
3. % 取余运算
"""
a = 20
b = 10
print(a / 3, a // 3, b / 3, b // 3)
print(ord("你"))
print(chr(20320))
'''
数据类型的转换：
1. str-> int int(arg) 如果是字符串'9.9'会报错
2. str-> float  float(arg)
3. int-> str  str(arg)
4. float-> str str(arg)
5. float-> int int(arg)
6. int->float  float(arg)
7. bool->int True:1  False:0
8. bool->float True:1.0  False:0.0
9. bool->str  True:'True'  False:'False'
'''