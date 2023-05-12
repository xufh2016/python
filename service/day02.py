super_star = ['michale jordan', 'kobe bryant', 'allen iverson', 'tracy ']
aa = type(super_star)
print(aa)
print(len(super_star))
print(super_star[-1])
# append添加元素到队列后面
super_star.append("lebron james")
# insert添加元素到指定索引位置
super_star.insert(1, "curry")
print(super_star)
# pop 删除
aa = super_star.pop()
print(aa)
print(super_star)
# 元组类型，tuple 类似list，但元组不能修改
market = ('likelai', 'guohuo', 'liqun')
print(type(market))
print(market[0])
print(market[-1])