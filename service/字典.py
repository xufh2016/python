rows = int(input('输入列数： '))
print("打印空心等边三角形，这里去掉if-else条件判断就是实心的")
for i in range(0, rows + 1):  # 变量i控制行数
    for j in range(0, rows - i):  # (1,rows-i)
        print(" ", end='')
        j += 1
    for k in range(0, 2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("*", end='')
                else:
                    print(" ", end='')  # 注意这里的", end='' "，一定不能省略，可以起到不换行的作用
            else:
                print("*", end='')
        else:
            print(" ", end='')
        k += 1
    print("")
    i += 1
