# python中的dict也就是java中的map，是键值对的存储
# 这样定义一个dict类型,和json类似
score_map = {"michael": 88, "tracy": 87, "james": 98, "curry": 99, "michael": 100}  # 如果key相同，那么最后赋值的将覆盖前面的值
print(score_map)
if "michael" in score_map:
    print(score_map["michael"])
else:
    print("这个key不存在")
names = score_map.keys()
print(names)
print(type(names))  # dict_keys类型
if score_map.get("allen"):
    print(score_map["allen"])
else:
    print("key allen is not exist")
# dict内部存放的顺序和key放入的顺序是没有关系的。dict有一下特点：1、查找和插入的速度极快，不会随着key的增加而变慢；2、需要占用大量内存，内存浪费严重
# dict的key必须是不可变对象，这是因为dict根据key来计算value的存储位置，是通过hash算法来计算的。
# 在python中，字符串、整数等都是不可变的，因此可以放心的作为key。而list是可变的，不能作为key使用
#################################################set#################################################
"""Python 还包含了一个数据类型 —— set （集合）。集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），
intersection（交），difference（差）和 sysmmetric difference（对称差集）等数学运算。"""
# set 会自动过滤重复 set的定义必须是  变量名=set([])
s = set([4, 44, 1, 2, 2, 33, 3, 33, 3])
# 重复添加，不会有任何效果，返回为None
print("添加重复：", s.add(2))
print(s)
# print(type(([1, 23, 4])))
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作