# str_fild = 'a'
# class MyObj:
#     # global str_fild
#     int_fild = 8
#     str_fild = 'string'
#
# print('MyObj.str_fild',MyObj.str_fild)
#
# obj1 = MyObj()
# obj2 = MyObj()
# print('obj1.str_fild', obj1.str_fild)
# print('obj2.str_fild', obj2.str_fild)
# obj2.str_fild = 'asdaf'
# print('obj1.str_fild', obj1.str_fild)
# print('obj2.str_fild', obj2.str_fild)
# MyObj.str_fild = 'my'
#
# print('obj1.str_fild', obj1.str_fild)
# print('obj2.str_fild', obj2.str_fild)
# print('MyObj.str_fild',MyObj.str_fild)

class Person:
    a_stat = 10
    def __init__(self, name='no_name', age=18):
        self.name = name
        self.age = age
    def print_info(self):
        print(self.name, 'is', self.age)

    @classmethod
    def person(cls):
        print('classMethod()')

    @staticmethod
    def stat_method():
        a_stat = 10
        print('ss')

john = Person('John', 22)
Person.print_info(john)
# Person.print_info(Person())

class ss:
    pass
s = ss()
s.age = 2
s.name = 's'
Person.print_info(s)
john.print_info()
Person.person()

class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return 'Ractangle(%.1f, %.1f)' % (self.side_a, self.side_b)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle(%.1f)' % self.radius # 12

    @staticmethod
    def from_rectagle(rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return Circle(radius)

    @classmethod
    def from_rectagle_class(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)

class Incap:
    def __init__(self):
        self.__private_attribute = 1

    def get_privet(self):
        return self.__private_attribute

    @property
    def private_attribute(self):
        return self.__private_attribute

    @private_attribute.setter
    def private_attribute(self, value):
        if value < 100:
            self.__private_attribute = value
        else:
            raise TypeError('больше 100')



class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return "Complex({!r}, {!r})".format(self.real, self.imaginary)

    def __str__(self):
        return "{}{:+d}i".format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        return self + (-other)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not self == other


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class LockAttr:
    def __init__(self):
        self.password = None
    def __getattribute__(self, item):
        if item == 'secret_field' and self.password == 'qwerty':
            return 'secret_place'
        else:
            return object.__getattribute__(self, item)

def main():
    pass
    # rec = Rectangle(3, 5)
    # print(rec)
    # f_c = Circle(1)
    # print(f_c)
    # s_c = Circle.from_rectagle_class(rec)
    # print(s_c)

    obj = Incap()
    print(obj.get_privet())
    print(obj._Incap__private_attribute)

if __name__ == '__main__':
    main()