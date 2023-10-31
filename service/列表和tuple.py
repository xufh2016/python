# classmates = ["Jordan", 'kobe', """james""", '柳岩']
# print(type(classmates))
# print(classmates)
# print(f'列表的长度是{len(classmates)}')
# a = 10
# print(20//3) # 地板除只有舍，没有入
a = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# print(a)
# zhongguo = "中国"
# print(len(zhongguo))
# print(len('中国'.encode("utf8")))
# # encode()用来将str编码为bytes类型  主要要指定编码方式，中文必须用u8

stars = ("michael jordan", "james", "kobe", "michael jackson")
# stars[0] = "柳岩"  tuple一旦初始则不能修改，tuple类型：元组类型
print(stars)
print(f"stras 的数据类型是：{type(stars)}")
# python在定义只有一个元素的元组类型时，必须加一个逗号“，”
super_stars = "lijing,", 'english', 'linzhiling', 'wangxiaoer', 'sadingding', "lucy"
print(f"super_stars 的数据类型是{type(super_stars)}")
students_score = {"xiaozhang": 80, "xiaowang": 99, "xiaoli": 66}
# a = tuple(students_score
print(super_stars[1:6:2]) # 切片 tuplename[start : end : step] start 表示起始索引，end 表示结束索引，step 表示步长。
e_tuple = ()
e_tuple = "monday", "星期二", "星期三" # 元组可以重新赋值，但不能新增删除修改
print(e_tuple)
