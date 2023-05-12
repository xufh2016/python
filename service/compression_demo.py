# 推导式
names = ["michael", "kobe", "james", "curry", "durant", "tm", "aj"]
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
######################
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

##############字典推导式##############
lists = ['google', 'alibaba', "Runoob", "Taobao"]
newDict = {key: len(key) for key in lists}
print(newDict)

###################
newSet = {i ** 2 for i in (1, 2, 3, 4)}
print(newSet)

'''元组推导式'''
a = (x for x in range(1, 10))
print(a)

print(tuple(a))