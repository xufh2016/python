# 迭代器
## 定义一个迭代器
from collections.abc import Iterable

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
lista = [1, 2, 5, 7, 9, 2]
for index, value in enumerate(lista):
    print(f"索引值是：{index}", f"当前索引对应的值是：{value}")
# it = iter(lista)
# print(type(it))
# print(next(it))
# print(next(it))
'''for 循环遍历迭代器'''
# for i in it:
#     print(i, end=" ")
"""while 循环遍历迭代器"""
# n = len(lista)
# while n > 0:
#     print(next(it), end=" ")
#     n -= 1
a = {"name": "zhangsan", "data": 1, "msg": "ok"}
if isinstance(a, Iterable):
    print("这是一个可迭代对象")
    for x, y in a.items():
        print(x, y)
else:
    print("这不是一个可迭代对象")

import os

newlist = [d for d in os.listdir('../../')]
print(newlist)
