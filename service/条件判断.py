# age = 4
# if age >= 18:
#     print("成人")
# elif age >= 6:
#     print("儿童")
# else:
#     print("幼儿")
# # if语句执行有个特点，它是自上而下执行，如果某个判断为true，会执行与该判断对应的代码块，会忽略掉剩下的elif和else。这点很重要
'''
注意：if条件判断语句从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行

需求：
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
'''

weight = 120
height = 1.82

bmi = weight / height ** 2

if bmi >= 32:
    print("严重肥胖")
elif 18.5 < bmi <= 25:
    print("正常")
elif 25 < bmi <= 28:
    print("过重")
elif 28 < bmi < 32:
    print("肥胖")
else:
    print("过轻")
