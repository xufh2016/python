'''
函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部变量状态不确定，同样的输入，可能得到不同的输出，因此这种函数是有副作用的。

函数式编程的一个特点就是：允许把函数本身作为参数传入另一个函数，还允许返回一个函数。

Python对函数式编程提供部分支持，由于python允许使用变量，因此，python不是纯函数式编程语言


'''
from functools import reduce

'''
可见，abs(-10)是函数调用，而abs是函数本身。

函数本身也可以赋值给变量，即：变量可以指向函数。

函数名其实就是指向函数的变量！对这个的理解非常重要


高阶函数是不是可以这么理解，一个函数在定义时，入参中的参数有函数的时候那么这个函数就是高阶函数

编写高阶函数的目的就是让函数的参数能够接收别的函数

把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
'''


def abs_add(x, y, function):
    """
    求两个数的绝对值的和
    :param x:
    :param y:
    :param function: 绝对值函数
    :return:
    """
    return function(x) + function(y)


a = abs_add(-5, 6, abs)
print("111111111--------------->", a)


def self_power(x):
    return x ** 2


def self_add(x, y):
    return x + y


def self_chengfa(x, y):
    return x * y


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(type(1))
print(type(lista))
ll = map(self_power, lista)

print(type(ll))
print(list(ll))
# for l in ll:
#     print("map---->", l)

'''
关于reduce函数
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
'''
xx = reduce(self_chengfa, lista)  # reduce函数中的第一个参数是一个function，这个function必须是接收两个参数
print(xx)

list_name = ['adam', 'LISA', 'barT']


def upper_lower_case(x):
    return x.capitalize()


map1 = map(upper_lower_case, list_name)

print(list(map1))


def is_odd(x):
    """
    保留奇数
    :param x:
    :return: true 保留，false：删除
    """
    return x % 2 == 1


lll1 = filter(is_odd, lista)
print(list(lll1))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(name):
    pass