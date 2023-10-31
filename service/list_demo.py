import operator

# list_a = [1, 2, 3, 4]
list_b = ["a", 169, "170", "v", "hello", 4, 55, 33]

a = list_b.copy()
print(a == list_b)

# a = list_b.pop(1)
# print(a)
# print(list_b)
# c = list_b.remove("v") #remove不会返回一个数这是和pop的区别
# print(c)
# print(list_b)
# list_c = list_a + list_b
# print(list_c)
# list_d = ["python"]
# print(list_d * 3)
# print(list_d)
#
# print(operator.eq(list_a, list_b))
# # print(max(list_b)) max不能数字类型和字符串类型同时比较
# 列表可以作为一个堆栈使用，append()方法可以把一个元素添加到堆栈顶。不指定索引的pop()方法可以把一个元素从堆栈顶释放出来。