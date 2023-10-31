'''
可以被next（）函数调用并不断返回下一个值的对象称之为迭代器：Iterator

Iterator的计算是惰性的，只有在需要返回下一个数据时，才有进行计算

凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next（）函数的对象都是Iterator类型，它们表示一个惰性计算的序列

'''
from collections.abc import Iterable, Iterator


def it_():
    yield 1
    print("stp 1")
    yield 2
    print("stp 2")


a = it_()
print(next(a))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(next(a))
print("---------------------------------------------------------------------------------------------------")

list2 = [1, 2, 'a', 11, "ad123ad"]
# print(isinstance(list1, Iterator))
# print(isinstance(list1, Iterable))
# print(isinstance(iter(list1), Iterator))

print("------------------------------------------------分割线------------------------------------------------")


def for_2_while(list1):
    """
    使用iter模拟for循环
    :param list1:
    :return:
    """
    if not isinstance(list1, (list, str, tuple, dict, set)):
        return
    it = iter(list1)
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            break

for_2_while(
    list2
)
