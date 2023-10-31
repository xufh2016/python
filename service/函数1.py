import math

"""
python的函数定义使用def 除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数。
1、默认参数：
   a、
"""


def add(x, y):
    return x + y


# a = add(1, 2)
# print(a)


def my_abs(x):
    """
    自定义一个绝对值函数
    :param x:
    :return:
    """
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs("a"))


def multi_results(x, y):
    """
    多个返回值时，实际上返回的是一个元组类型tuple
    :param x:  参数一，
    :param y:  参数二
    :return:  x+y  y-x
    """
    return x + y, y - x


# a = multi_results(2, 5)
# print(a)
# print(type(a))


def quadratic(a, b, c):
    """
    求二元一次方程 ax**2+bx+c=0 的两个解
    :param a:
    :param b:
    :param c:
    :return:
    """
    if not isinstance(a, (int, float)) \
            and not isinstance(b, (int, float)) \
            and not isinstance(c, (int, float)):
        raise TypeError("bad param")
    if (b ** 2 - 4 * a * c) > 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        y = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return x, y
    else:
        raise TypeError("参数b过小")


# print(quadratic(3, 9, 5))

# print(math.sqrt(0))


def power(x, y=1, n=2):
    print(y)
    """
    默认参数一定要使用不可变对象
    幂运算，x的n次幂
    :param x:
    :param n:
    :return:
    """
    res = 1
    while n > 0:
        n -= 1
        res = res * x
    return res
    # return x ** n


print(power(3, n=4))  # 这种方式需要提供参数名


# print(3 ** 3)


# 定义可变参数的函数
def variable_param(name, *cities, **other):
    """
    测试可变参数的函数定义，*cities是可变参数，可变参数在函数调用时自动组装成一个tuple类型
    **other关键字参数 会被封装成一个dict
    :param name:
    :param cities:
    :param other
    :return:
    """
    print(type(cities))
    for city in cities:
        print(f'hello,{name} in {city} , other: {other}')


a = {"job": "Java"}
variable_param("zhangsan", "qingdao", "wuhan", "beijing",
               **{"job": "python", "likes": "football"})  # 这样入参，在函数内部对关键字参数的改变不会影响到外面的a

variable_param("lisi", "dongjing", "niuyue", **a)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如只接受city和job作为关键字参数。可以如下定义
def person(name, age=18, *, city, job):
    """

    和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。命名关键字参数必须传入参数名，这和位置参数不同
    :param name:
    :param age:
    :param city: 命名关键字参数
    :param job:  命名关键字参数
    :return:
    """
    pass


def person1(name, age, *args, city, job='Engineer'):
    """
    city和job会被当作为命名关键字参数
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了。命名关键字参数必须传入参数名，这和位置参数不同
    :param name:
    :param age:
    :param args: 可变参数
    :param city: 命名关键字参数
    :param job:  命名关键字参数,但是设置了默认值，在入参时可以不入参
    :return:
    """
    pass


def all_params(name, age=18, *likes, **scores):
    """
    参数组合:参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    :param name:     必选参数
    :param age:      默认参数
    :param likes:    可变参数
    :param scores:   关键字参数
    :return:
    """
    pass
