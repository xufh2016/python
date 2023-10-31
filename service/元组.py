#
# tup = ("Python", 'Java', "showMeAI", "golang")
# print(id(tup))
# tup1 = ["1", '2', "3", "5"]
# # tup = tup + tup1  # 其实是已经改变了地址了，对象发生了改变
# print(tup)
# print(id(tup))
# print(tuple(tup1))
# 一个变量被赋多个值时，当前变量会变成元组
t = 123, 234, "hello"
print(t)
print(type(t) )