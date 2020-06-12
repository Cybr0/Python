# with open('1.txt', encoding='utf8', mode='w+') as file:
#     tmp = 'first str\nsecond str\nthird str'
#     file.write(tmp)
#     file.seek(1)
#     t = file.read()
#     print(t)
#
# d = {'k': [1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(*d['k'][2]['k2'][1]['tough'][2])
# f = 1, 2
# print(f)
import io
import time

# path = 'try_bootstrap/index1.html'
# f = open(path, mode='r', encoding='utf-8')
# doc = f.read()
# print(doc)
# f.close()
# f = open('try_bootstrap/index.html', mode='w+', encoding='utf-8')
# f.write(doc)
# f.close()

'''
================================================================================

'''


# def foo(a):
#     a += 1
#
# a = 1
# foo(a)
# print(a)


class List:
    class _Node:
        __slots__ = ('value', 'next')

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class _NodeIterator:
        def __init__(self, first):
            self._next_node = first

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration
            value = self._next_node.value
            self._next_node = self._next_node.next
            return value

    def __init__(self):
        self._head = self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def __repr__(self):
        return f'{[i for i in self]}'

    def append(self, value):
        node = List._Node(value)
        if len(self) == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._length += 1

    def extend(self, iterable):
        for _ in iterable:
            self.append(_)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        # if 0 > index or index >= len(self):
        if not 0 <= index < len(self):
            raise IndexError('List index out of range')
        node = self._head
        for _ in range(index):
            node = node.next
        return node.value

    # def __iter__(self):
    #     return List._NodeIterator(self._head)
    def __iter__(self):
        node = self._head
        for _ in range(len(self)):
            yield node.value
            node = node.next


def data_from():
    while True:
        data = input('Enter data:')
        print('print:', data)
        print()
        yield


def doing_smg():
    while True:
        yield from data_from()


def main():
    start = 1
    while True:
        if start % 100000 == 0:
            print('work')
        f = doing_smg()
        next(f)
        start += 1



if __name__ == '__main__':
    main()