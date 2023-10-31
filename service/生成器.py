"""

1、生成器：generator，一边循环一边计算的机制
2、创建方法：
   1、第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
   2、如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
"""

g = (i + 3 for i in range(10))
for i in g:
    print(i)

x, y = "long", "short"  # 这种方式python会临时或永久的建立成tuple来保存元素
print(x)
print(y)

ss = "long"
ll = a, b, c, d = ss
print(a)
print(b)
print(c)
print(d)
print(ll)
print(type(ll))
