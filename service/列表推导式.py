# 5>3?print("haha"):print("ssssss")
# 三目表达式。类别 ?:
print("hahaha") if 5 > 3 else print("xixixi")
# range 函数 arg1：起始，arg2 结束值  arg3：步长
# 列表推导式：最终得到的是一个列表
list1 = [i + 1 for i in range(1, 100, 2)]
print(list1)
ll = ["34", "11", "lq", "lucky","hh"]
# isalpha()判断全字母
newll = [item for item in ll if item.isalpha()]
print(newll)
newll = [word.title() if word.startswith("l") else word.upper() for word in ll]
print(newll)