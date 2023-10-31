# 不定长参数会收集成元组，元组的特性是不可变的
def get_sum(*args):
    result = 0
    for item in args:
        result += item

    print(args)
    return result


rand_list = [1, 3, 11, 5, 67, 98, 34, 77]
print(*rand_list)# 拆包

a = get_sum(1, 2, 3)
print(a)
