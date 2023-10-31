'''


'''
# import random
#
# '''
# times: 循环次数
# s：定义的时候叫做默认值参数
# '''
#
#
# def generate_verification_code(times, m='',
#                                s='qwertyuiopasdfghjklzxcvbnmADSFGHKJL:QWERTYUIOPZXCVBNM<>=;1234567890-_+!@#$%^&'):
#     code = ''
#     for i in range(times):
#         r = random.choice(s)
#         code += r
#     return code
#
#
# # 调用函数，注意要有括号，否则只是将函数加载到内存中，但并未开始执行函数
# print(generate_verification_code(5, s='adkjs;akdpfoiekr;lakdfjapfapgja'))  # 调用的时候，s就叫做关键字参数
#
# list1 = [23, 45, 33, 66, 78, 21, 99]
# # 列表推导式
# list2 = [item for item in list1 if item > 50]
# print(list2)


def scope_test():
    def do_local():
        spam = "local spam"  # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local() # 这个地方就把它理解为下面的test函数那种就可以了
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

a="asdf"
def test():
    a="bcd"
test()
print(a)