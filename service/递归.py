# i = 0
#
#
# # python中递归的最大深度是996，超过就会抛出RecursionError
#
# def a():
#     global i
#     i += 1
#     print("----------------------------------a----------------------------", i)
#     if (i >= 996):
#         return
#     a()
#
#
# a()
def test1(i):
    if i == 10:
        return 10
    else:
        return i + test1(i + 1)


res = test1(9)
print(res)
