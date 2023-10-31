# 定义一个装饰器，装饰器也是一个有些特殊的函数，但要有入参。
def decorator(func):  # 只函数名入参，说明是入参函数的地址
    print("-------------------------------1-----------------------")

    def wrapper(*args, **kwargs):
        pre_price = func(*args, **kwargs)  # 加了括号以后，表示函数调用
        print('粉刷房子')
        print('铺地板')
        print('买家具')
        print('精装修房子')
        price = 20000
        return price + pre_price

    print("-------------------------------2-----------------------")
    return wrapper


# 使用装饰器 house会自动作为参数传入定义的装饰器中。原函数有返回值，那么装饰器一定要有返回值
@decorator
def house(price):
    print("买了一个毛坯房")
    return 50000


# 函数调用
total_price = house(50000)
print(total_price)
