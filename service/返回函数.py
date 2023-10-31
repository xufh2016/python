def lazy_sum(*args):
    """
    闭包的实例，
    返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
    :param args:
    :return:
    """
    def sum():
        res = 0
        for arg in args:
            res += arg
        return res

    return sum


f = lazy_sum(1, 3, 5, 11, 22)
print(f())
