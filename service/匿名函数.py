res = lambda arg1, arg2: arg1 + arg2
print(res(1, 2))
'''
res = lambda arg1, arg2: arg1 + arg2
就相当于如下函数
关键字lambda表示匿名函数，冒号前的arg1、arg2表示函数的参数
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
'''


def sum(x, y):
    return x + y


res = lambda x: x % 2 == 1


def is_odd(x):
    return x % 2 == 1

print(is_odd.__name__)
print(type(is_odd))
print(res(3))
