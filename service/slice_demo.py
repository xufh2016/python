#  实现去除字符串首尾空格的函数
def trim(s):
    if " " in s:
        return s[1:-1]
    else:
        return s


print(trim(" hello world "))
