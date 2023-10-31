list1 = [('tom', 19), ('tony', 22), ("lucy", 18), ("michael", 45)]

res = filter(lambda item: item[1] > 20, list1)

print(list(res))
