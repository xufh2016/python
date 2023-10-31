'''
定义一个有返回值的函数
return 后面可以是一个值，也可以是多个值，如果多个值，会将多个值封装到一个元组中，将元组作为整体返回
'''


def add(a, c):
    return a + c


def sum(*args):
    """
    求和运算
    :param args: 数字
    :return:  得到的和
    """
    total = 0
    for item in args:
        if isinstance(item, int):
            total += item
        else:
            continue
    return total


res = sum(2, 3, 4, 5, 6, " 8", 4)
print(res)

b = add(2, 4)
print(b)


# 定义一个无返回值的函数
def void_say(a, b):
    a + b
    print(a, b)


res1 = void_say(1, 2) # None==fasle
if res1:
    print(True)
else:
    print(False)



print(res1)
