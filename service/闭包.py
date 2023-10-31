def outer(n):
    a = 10

    def inner():
        b = a + n
        print("内部函数：", b)

    return inner


a = outer(10)
a()
