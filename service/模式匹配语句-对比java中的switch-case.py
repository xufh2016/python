score = 'A'
# match score: python9版本不提供match...case
a = range(100)
b = list(a)
print(b)
res = 0
for i in b:
    res += i
print(res)

res1 = 0
n = 99
while n > 0:
    if n % 2 == 1:
        res1 += n
    n = n - 1
print(res1)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    if name == 'Adam':
        break
    print(f"Hello,{name}")
print("------------------------------break end,continue on-------------------------------------")
for name in L:
    if name == "Lisa":
        continue
    print(f"Hello,{name}")
# continue语句通常都必须配合if语句使用