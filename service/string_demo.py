# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]
# city = "中国山东青岛城阳"
# print(city[2:-1:2])
# a = isinstance(1, int)
# print(a)
# a = 2 + 1j
# print(type(a))
# print(complex(2, 1))
# print(type((1,)))
# a = set({1, 2})
# a = set(["a", 12])
# print(a)
url = "https://www.hxstrive.com/subject/rabbitmq/1038.htm"
'''截取https'''
last_index = url.find(":")
begin_index = url.find("")
print(last_index, begin_index, end=" ")
print(url[begin_index:last_index])
# 是完全匹配
print(url.find("1034"))
a = input("请输入")
print(a.isdigit())
print(a.isalnum())
print(a.startswith("htm"))