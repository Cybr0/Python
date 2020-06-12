import math

values = [5, 6, 7, 9, 2, 8, 1]


def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('Next value received:', value)


class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        # elif index in 'qwertyuiopasdfghjklzxcvbnm':
        #     return index
        else:
            raise IndexError


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.begin = 0
            self.end = first
        else:
            self.begin = first
            self.end = second

        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be Zero!')

        self.length = math.ceil((self.end - self.begin) / self.step)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.begin + index * self.step
        else:
            raise IndexError('MyRange index out of range!')

    # def __iter__(self):
    #     return RangeIterator(self)
    def __iter__(self):
        current = self.begin
        for _ in range(len(self)):
            yield current
            current += self.step

    def __repr__(self):
        return 'MyRange({}, {}, {})'.format(self.begin, self.end, self.step)


class RangeIterator:
    def __init__(self, range_instance):
        self.range = range_instance
        self.next_value = range_instance.begin

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value >= self.range.end and self.range.step > 0 or \
                self.next_value <= self.range.end and self.range.step < 0:
            raise StopIteration

        result = self.next_value
        self.next_value += self.range.step

        return result


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

    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._length = 0

        if iterable is not None:
            self.extend(iterable)

    def __repr__(self):
        return f"List {[i for i in self]}"

    def __len__(self):
        return self._length

    def append(self, value):
        node = List._Node(value)

        if len(self) == 0:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    # def __iter__(self):
    #     return List._NodeIterator(self._head)
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next


def main():
    # 1
    # my_for(range(1), loop_body)
    # iterable = SimpleIterable()
    # for value in iterable:
    #     print(value)
    # # print(iterable['a'])
    #
    # print('MyRange')
    # for value in MyRange(end=10):
    #     print(value)

    # 2
    # for value in MyRange(10, 5, -1):
    #     print(value)
    # print('len=', len(MyRange(10, step=3)), sep='')

    # 3
    print('worked')
    l = List([1, 'rr', 3])
    print(l)
    print(l._tail.value)



if __name__ == '__main__':
    main()
