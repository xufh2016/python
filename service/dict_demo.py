a = {}
# print(isinstance(a, dict))
a = {"name": "zhangsan", "data": 1, "msg": "ok"}
# dict in只能判断key是否在字典中
print("name" in a)
print("zhangsan" in a)
print(dict.items(a))
b = dict.fromkeys(a)
print(b)

print(a)
print(a.keys())
print(a.get("name"))
a = dict([("name", "lijing"), ("age", 30), ("career", "公务员")])
print(a)
