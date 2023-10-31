'''
if
if...else

if ...elif...else

if...elif...elif ... ...else

'''

# condition = input("请输入：y/n")
# if condition == 'y':
#     print(4)
# else:
#     print(5)

# 猜数游戏

# 随机数
import random


def guess_number():
    """
    猜数字游戏
    :return:
    """
    ran = random.randint(1, 10)
    print(ran)
    flag = False
    while not flag:
        number_in = input("请输入你要猜的数：")
        if int(number_in) == ran:
            print("猜对了")
            flag = True
        else:
            print("猜错了了")


####################################################################
print("####################################################################")


def sale_price():
    sale = float(input("请输入销售金额："))
    if 1 <= sale <= 5:
        print("奖励1k rmb")
    elif 5 < sale <= 10:
        print("奖励笔记本电脑")
    elif 10 < sale <= 100:
        print("奖励iPhone15 plus 1TB + macbook pro")
    elif sale > 100:
        print("奖励特斯拉")
    else:
        print("别做梦了~~~~~~~~~~~~~~")


# while True:
#     sale_price()

people_list = []


def comp_sys():
    print("欢迎进入人员管理系统")
    choice = input("""请选择功能:
       1、添加员工
       2、删除员工
       3、查找员工
       4、修改员工信息
       5、退出系统
       """)
    if choice == '1':
        print("添加员工")
        new_per_name = input("请输入员工姓名：")
        people_list.append(new_per_name)
    elif choice == '2':
        print("删除员工")
        new_per_name = input("请输入员工姓名：")
        people_list.remove(new_per_name)
    elif choice == '3':
        print("查找员工")
        new_per_name1 = input("请输入员工姓名：")
        if new_per_name1 in people_list:
            print("找到了")
        else:
            print("没有找到")
    elif choice == '4':
        print(people_list)
    elif choice == '5':
        print("退出系统~~~~~~~~~~~~~~")
        exit()


while True:
    comp_sys()
