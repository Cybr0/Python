class Base1:
    def method(self):
        print('base1')
        print(type(self).__name__)

class Base2:
    def method(self):
        print('base2')
        print(type(self).__name__)

class Dir(Base1,Base2):
    def method(self):
        print('Dir')
        print(type(self).__name__)


# d = Dir()
# print(type(d.method))
# print(type(Dir.method))

class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False
        print('__init__.Animal')

    def print_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run:', self.can_run)
        print('Can fly:', self.can_fly)
        print()

class Horse(Animal):
    def __init__(self):
        # super().__init__()
        Animal.__init__(self)
        self.can_run = True
        print('__init__.Horse')

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)
        # super().__init__()
        self.can_fly = True
        print('__init__.Bird')

class Pegasus(Horse, Bird):
    def __init__(self):

        Bird.__init__(self)
        Horse.__init__(self)
        # super().__init__()
        print('__init__.Pegasus')

if __name__ == '__main__':
    # horse = Horse()
    # horse.print_abilities()
    # bird = Bird()
    # bird.print_abilities()
    pegasus = Pegasus()
    pegasus.print_abilities()