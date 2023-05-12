# 函数的重命名：变量名=函数名  注意函数名后面不要加()
# from day01 import a, ccc


# from service import day01
#
# print(a)
# print(ccc)
# c = abs
# b = c(-56)
# print(b)


# 自定义函数 函数的定义需要 使用关键字 def  函数名(参数列表):  函数体
# def my_abs(arg):
#     if not isinstance(arg, (int, float)):
#         raise TypeError('参数类型错误')
#     if arg > 0:
#         return arg
#     else:
#         return -arg
#
#
# # 验证自定义函数
# print("自定义函数求绝对值：", my_abs(-3))


# 多参数 ,设置默认参数，默认参数需要放到参数列表的最后
# def my_test_multi_args(name, gender, age=12, city='青岛', *v, **b):
#     print("name: ", name)
#     print("gender: ", gender)
#     print("age: ", age)
#     print("city: ", city)
#     print("b: ", b)
#     print("v: ", v)
#
#
# my_test_multi_args("kobe", "男")
# my_test_multi_args("lucy", "female", v=(2, 3, 4), b={"nba:superstar": "michael jordan"})
# :切片操作符
list = ["jordan", "kobe", 'curry', 'james', '''durant''', 'oneal']
print(list[:3])
print(type(list[0:1]))