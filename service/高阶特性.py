l = list(range(100))
# print(l)
# print(f"只取奇数{l[1:100:2]}")
# print(f"只取11到20的数{l[11:21]}")
# print(f"取后20个数{l[-20:]}")
# print(f"所有数，每隔4个取{l[::4]}")
# print(f"前十个，每隔两个取一个{l[:10:2]}")
t = 1, 2, 3  # 元组类型
print(type(t))
print(t[1:3])
'''
python中没有关于字符串的截取函数，只需要切片一个操作就可以完成
'''
dict1 = {"name": "zhangsan", "age": 12, "job": "student", "likes": ["football", "basketball"], "star": "liuyan"}
for k, v in dict1.items():
    if isinstance(v, (list, tuple)):
        for item in v:
            print(f"{k}---------------{item}")
    else:
        print(f"{k}------{v}")
