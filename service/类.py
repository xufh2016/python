# 类的方法和普通的函数的唯一区别就是：类的方法，他们必须有一个额外的第一参数名称，按惯例它的名称是self
'''
在类的内部定义的成员方法，必须包含参数self且为第一个参数，self代表的是类的实例。
self的名字并不是规定死的，也可以使用this，但建议还是按照约定使用self
'''


class Animal(object):
    # 构造器 ,实际上不是真的构造器，是在对象初始化后（对象创建好后）用来初始化变量的
    def __init__(self, species):
        self.__a = species

    # __new__()方法是在向内存成功申请了一块空间，申请完以后，通过__init__方法将属性放到空间中，来完整的表达一个对象
    def __new__(cls, *args, **kwargs):
        print("-----------new------------")
        return object.__new__(cls)

    def show_species(self):
        """
        显示动物的生物学种类
        :return:
        """
        animal_species = self.__get_species()
        print(animal_species)
        # 类内调用类中的方法，需要使用self.方法名
        self.__bark()

    def __get_species(self):
        return self.__a

    def __bark(self):
        animal_species = self.__get_species()
        print(f"{animal_species}的叫声是汪汪汪~~~~~~~~~~~~~~~")

    def __str__(self):
        """
        可以这样理解：理解为Java的toString方法。但python中的这个方法必须返回一个字符串
        :return:
        """
        return f"动物的生物学种类是：{self.__a}"


dog = Animal("犬科")
print("haha~~~~~~~~~~~~来了一种", dog, end="")


# dog.show_species()


class Dog(Animal):
    def __init__(self, types, species):
        super().__init__(species)
        self.__types = types


class Person:
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def talk(self):
        print("%s的年龄是 %d 岁。" % (self.name, self.age))
