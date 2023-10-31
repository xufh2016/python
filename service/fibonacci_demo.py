# a, b = 0, 1
# while b <= 100:
#     print(f"b的值是“：{b}")
#     a, b = b, a + b
#
# print("===============================")
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a # 到了yield修饰的a这儿，a的值就被返回到某个地方了，但当前下面的语句不会停止
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
