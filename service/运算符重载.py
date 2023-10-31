class MyVector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return MyVector(self.a + other.a, self.b + other.b)


v1 = MyVector(2, 10)
v2 = MyVector(5, -2)
print(v1 + v2)
