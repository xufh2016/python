
# kwargs 是指key:value组合的不定长,关键字参数，是一个字典入参
def show_book(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
    print(kwargs)

# 如下使用
show_book(name="zhangsan",name1="lis")
show_book(name="zhangsan",age="11")
show_book(book="harry poter",author="jk rolin")
