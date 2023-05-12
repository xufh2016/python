# 空元祖
a = ()
print(type(a))
print(id(a))
# 这个地方相当于给变量a重新赋值了一个新的元组数据
a = (1, "a", 4, 2)
b = (1, "a", 4, 2)
print(a)
print(id(a))
# TypeError: 'tuple' object does not support item assignment
# a[0] = 10
print(a is a)
