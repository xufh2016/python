from collections.abc import Iterable

print(isinstance("abc", Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
######################################列表生成式#################################

print([x ** 2 for x in range(100)])
print([x ** 2 for x in range(100) if x % 2 == 1])
'''
1、列表生成式是用来创建list的生成式
2、列表生成式的结构是在一个中括号里包含一个表达式，然后是一个或多个for语句，然后是0个或多个if语句。列表表达式可以是任意的，你可以在列表中放入任意类型的对象，返回结果将是一个新的列表
3、格式：[outer_exp for outer_exp in input_list if outer_exp == ??]
4、在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
5、运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
'''
d1 = {"name": "zhangsan", "age": 18, "likes": "liuyan"}
print([k + "=" + v for k, v in d1.items() if not isinstance(v, (int, float))])
# isinstance()函数的第二个入参，当是多个值的时候那么必须明确写成tuple类型，如果只一个值的时候可以不显示写出tuple结构
list11 = ["asdf", "zhangsan", 12, 34, "isis", "rip", "ospf", 56]
list2 = [item.upper() for item in list11 if isinstance(item, str)]
print(list2)
