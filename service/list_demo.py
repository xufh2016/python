import operator

list_a = [1, 2, 3, 4]
list_b = ["a", 169, "170", "v", "hello", 4, 55, 33]
list_c = list_a + list_b
print(list_c)
list_d = ["python"]
print(list_d * 3)
print(list_d)

print(operator.eq(list_a, list_b))
# print(max(list_b)) max不能数字类型和字符串类型同时比较
