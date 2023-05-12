# 生成器表达式
# x = (x ** 2 for x in range(10))
# print(x)

# 列表推导式，也叫做列表生成式
i = [i for i in range(10)]
print(i)


def yahui():
    line = [1]
    while True:
        yield line
        line = [1] + [line[x] + line[x + 1] for x in range(len(line) - 1)] + [1]


print(yahui())
