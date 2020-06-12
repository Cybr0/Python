class Base:
    def method(self):
        print('Hello')

class Child(Base):
    def child_method(self):
        print('child_method')

    def method(self):
        print('Hello child')

# obj = Child()
# obj.method()
# obj.child_method()

class Figure:
    def __init__(self, side=0.0):
        self.side = side

class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)

class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)


class Horse():
    def run(self):
        print("i'm running.")
    def eat(self):
        print('Horse eat')

class Bird:
    def fly(self):
        print("i'm flying.")
    def eat(self):
        print('Bird eat')

class Pegasus(Horse, Bird):
    print('Hello')



class A:
    def meth(self):
        print('Method class:', __class__.__name__)
        print('Method class:', __class__)
        print('Instance class:', type(self).__name__)
        print('Instance class:', type(self))

class B(A):
    pass

def main():
    # square = Square(5)
    # triangle = Triangle(8)
    # figures = square.draw, triangle.draw
    # figures[0]()
    pass


    # p = Pegasus()
    # p.run()
    # p.fly()
    # p.eat()
    # print(Pegasus.__bases__)

    a = A()
    a.meth()
    print("#" * 50)
    b = B()
    b.meth()
    print("#" * 50)
    print(B.mro())


if __name__ == '__main__':
    main()