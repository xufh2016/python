'''
猜拳游戏，3局两胜
'''
import random


def cai_quan():
    p_counter = 0
    m_counter = 0
    n = 1
    while n <= 3:
        machine = random.randint(1, 3)
        person = int(input("请输入剪子（1）、包袱（2）、锤（3）\n"))
        if person == 1 and machine == 2 or person == 2 and machine == 3 or person == 3 and machine == 1:
            p_counter += 1
            print("人赢了~~~~~~~~~~~~~~~~")
        elif machine == 1 and person == 2 or machine == 2 and person == 3 or machine == 3 and person == 1:
            m_counter += 1
            print("机器赢了~~~~~~~~~~~~~~~~~")
        else:
            print("平局")
        # if p_counter == m_counter:
        #     n -= 1
        n += 1
    if p_counter > m_counter:
        print("hahahah~~~~~~~~~~~~")
    elif p_counter == m_counter:
        print("ooooooo~~~~~~~~~~~~")
    else:
        print("heiheihei~~~~~~~~~~~~~~~")
    # return p_counter, m_counter


# f = cai_quan()


# print(f[0])
# f[0]
def cai_quan_for():
    p_counter = 0
    m_counter = 0
    n = 1
    for i in range(3):
        machine = random.randint(1, 3)
        person = int(input("请输入剪子（1）、包袱（2）、锤（3）\n"))
        if person == 1 and machine == 2 or person == 2 and machine == 3 or person == 3 and machine == 1:
            p_counter += 1
            print("人赢了~~~~~~~~~~~~~~~~")
        elif machine == 1 and person == 2 or machine == 2 and person == 3 or machine == 3 and person == 1:
            m_counter += 1
            print("机器赢了~~~~~~~~~~~~~~~~~")
        else:
            print("平局")
        # if p_counter == m_counter:
        #     n -= 1
        n += 1
    if p_counter > m_counter:
        print("hahahah~~~~~~~~~~~~")
    elif p_counter == m_counter:
        print("ooooooo~~~~~~~~~~~~")
    else:
        print("heiheihei~~~~~~~~~~~~~~~")


# f = cai_quan_for()

def jiu_jiu():
    '''
    注意：range()函数
    1、
    九九乘法表
    :return:
    '''
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{j} * {i} = {i * j}', end='   ')
            if j == 9:
                print("\n")


# jiu_jiu()


def add_1_100():
    res = 0
    for i in range(1, 101):
        res += i
    return res


# f = add_1_100()
# print(f'最终结果是：{f}')
def game_shaizi(coins=10):
    while coins >= 5:
        coins -= 5
        shai_zi = random.randint(1, 6)
        p_number = int(input("请输入你猜的数字："))
        if p_number == shai_zi:
            print("猜对了")
            coins += 2
        else:
            print("猜错了")
            coins -= 1
    else:
        exit_flag = input("金币不足了，是否想退出y/n?")
        if exit_flag == 'y':
            exit()
        elif exit_flag == 'n':
            coins = int(input("金币不足，请充值："))
            game_shaizi(coins)


game_shaizi()
