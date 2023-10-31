#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这是一行注释，暂时无实际意义仅仅为了测试而已
# 变量本身类型不固定的语言称之为动态语言。
# 变量->栈内存；数据->堆内存
# print("hello world")
#
# a = 10
# ccc = '123'
# print("hello", "world")
# # print("please", "input", "your name:")
# name = input("please input your name:")
# print("your name is", name)
# age = eval(input("please input your age:"))
# if age >= 20:
#     print("haha~~~~~~~~~~~")
# else:
#     print("heiheihei~~~~~~~~~~~~~~~~~~")
# True
# print(5/3)
# print(3.2/3.1)
# ord函数获取单个字符的整数表示
# print(ord(b"z"))
# strs = "111111111"
# print(type(b"z")) # 加了b前缀表示的是bytes(字节)类型
str = "你好，中国"
ls = str.encode("gb2312")
en = str.encode("utf-8") # 用utf8编码 会编码成bytes类型
ll = en.decode("utf8") # 解码
print(en)
print(ll)
print(ls)
# stre = b"123b"
# length = len(stre)
# print(length)

r = 4.03
s = 3.14 * (r ** 2)
print(f'半径为:{r}的圆的面积是：{s:.4f}')
