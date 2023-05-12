'''
变量： 可以类比成容器
py是一门弱语言，变量声明的时候对数据类型不是很严格。
py中变量的类型取决于赋值的类型

""=''
格式： 变量名=值
1. 怎么起名？

2. 可以赋什么值

3. 有哪些数据类型

变量名的命名规范：
1、只能字母、数字、下划线,需要注意的是美元符$是绝对不可用的
2、不能以数字开头
3、不能使用关键字
4、严格区分大小写
5、开发过程中建议使用下划线命名法（snake case）
'''

#

# salary = 100.2222
# typ = type(salary)
# print(typ)
#
# money = '''shang'''
# print(type(money))
# msg = True
# msg = False
# 类型转换
print(bool(-0.01))
print(bool("1"))
print(bool([1, 2]))
print(bool(None))
print(bool((1,)))
print(bool(()))
print(bool({"1": 1}))
print(bool(0))
