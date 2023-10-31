a = 100


def test():
    a = 99
    global a
    a -= 80
    print(a)


test()
