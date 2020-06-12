import pickle
import reprlib


class Person(object):
    def __init__(self, name, age, siblings=None):
        self.name = name
        self.age = age
        self.siblings = siblings or []

    @reprlib.recursive_repr()
    def __repr__(self):
        return 'Person({name!r}, {age!r}, {siblings!r})'.format_map(self.__dict__)

    @staticmethod
    def make_siblings(first, second):
        first.siblings.append(second)
        second.siblings.append(first)


p = Person('John', 19,)
p2 = Person('Mellisa', 23,)
Person.make_siblings(p, p2)

with open('le_8_dir/example8_2.pkl', 'wb') as data:
    pickle.dump((p, p2), data)


with open('le_8_dir/example8_2.pkl', 'rb') as data:
    people = pickle.load(data)

print(people)

print('---------')
pickle_str = pickle.dumps([12, 11])
print(pickle_str)
print(type(pickle_str))
pickle_str = pickle.loads(pickle_str)
print('---------')
print(pickle_str)
print(type(pickle_str))
