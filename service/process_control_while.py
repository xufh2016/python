stus = ['Bart', 'Lisa', 'Adam']
attr = len(stus)
while (attr):
    # if attr <= 1:
    #     break
    attr = attr - 1
    print(stus[attr])
    print(attr)
print("------------------END-----------------")
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
