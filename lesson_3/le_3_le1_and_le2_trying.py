class Tmp:
    __instance = None

    def __init__(self, a=7, b=1):
        self.a = a
        self.b = b

    # def __new__(cls):
    #     if cls.__instance is None:
    #         cls.__instance = object.__new__(Tmp)
    #     return cls.__instance

    def __str__(self):
        return f'ab={self.a}{self.b}'

    def __getattribute__(self, item):
        if item == "q":
            exit('tmp.q = quit')
        return object.__getattribute__(self, item)

    def __add__(self, other):
        return Tmp(a=(self.a + other.a), b=(self.b + other.b))

tmp = Tmp()
print(id(tmp))
print(tmp)
print(tmp.__class__.__name__)
print(type(tmp).__name__)
print(Tmp.mro()[1].__name__)
tmp = tmp + Tmp(2, 83)
print(tmp)


def f(a):
    print(a)

def f(a, b):
    print(a, b)

