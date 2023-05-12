print("please input your age： ")
age = input() # input函数也叫阻塞型函数
if age:
    print('True,输入有效。。。。。。。。。。')
age = eval(age)
# 条件判断 ，条件后面一定要注意冒号（:）
# if语句自上而下执行，如果是在某个分支上为True，则执行完该判断对应的语句，就会忽略掉剩下的elif 和 else
if age >= 18:
    print("your age is ", age)
    print("you are an adult")
elif age >= 6:
    print("your age is ", age)
    print("teenager")
else:
    print("your age is ", age)
    print("kid")
# Practice BMI
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("过于肥胖")
# range()函数，半闭半开区间
for x in range(1, 101):
    print(x)
# range()函数，用来生成一个整数序列，再通过list()函数可以转换为list
'''
Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
'''
# 求1--100所有整数的和
# res = 0
# for i in range(1, 101):
#     res += i
# print(res)


# 求100以内奇数的和
res = 0
n = 99
while n > 0:
    res += n
    n -= 2
    if res > 2100:
        print("n 的值是：", n)
        print("现在的结果是：", res)
print(res)
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常必须配合if语句使用。
# 死循环
while True:
    print("hello world,this is python")
