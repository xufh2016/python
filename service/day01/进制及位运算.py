"""
1、二进制
2、八进制
3、十进制
4、16进制
5、36进制

"""
n = 149

# 转2进制
res = bin(n)  # 前缀是0b
print(res)  # 打印的是：0b10010101

# 转8进制
res = oct(n)  # 前缀是0o
print(res)  # 打印的是：0o225

# 转16进制
res = hex(n)  # 前缀是0x
print(res)  # 0x95

n1 = 0x95
result = int(n1)
print(result)
n = 0b10010101
result = int(n)
print(result)

result = bin(n1)
print(result)

'''
一定要注意一点：
1、位运算是针对二进制进行的运算
2、所有的位运算都是基于二进制的
这两点一定要牢记，很重要



'''

m = -5
res = bin(m)
print(res)

print(
    oct(-0b101)
)

print(int(-0o5))
print(int(-0b11111010))
'''
<<  左移  左移几位相当于原来的数乘以2的左移位数的次方运算，比如  12 左移 2位，相当于 12*2**2  （12乘以2的平方）

>>  右移 左移几位相当于原来的数除以2的左移位数的次方运算，比如  12 左移 2位，相当于 12/2**2  （12除以2的平方） 整除 不管余数
'''
print(3 << 5)
print(12 >> 2)

print(34 >> 4)
