# import collections.abc
import sys
# print(dir())
# print(dir(collections.abc.Sequence))
# print()
# print(dir(collections.abc.MutableSequence))
# print(dir())
# print(__file__)
l = [1, 2, 5, 6, 3, 9, 8, 2]
# z = zip(l, range(len(l)))
# print(l.__getitem__(slice(5, 1000, 10000)))
# print(list(z))
print(3 in l)
print(l.__contains__(3))

print(l)

l2 = [0, 2]
# l3 = l + l2
# print(l2)
# print(l3)
# print()
# l3[0] = 10
# l2[0] = 10
# print(l)
# print(l2)
# print(l3)


# l4 = l2 * 3
# l4[0] = 10
# print(l2)
# print(l4)
# l5 = list(l2) * 3
# l5[0] = 10
# print(l2)
# print(l5)


# print(l.index(2))
# print(l.count(2))
# print(l.__contains__(2))


l[0] = 5
l.__setitem__(0, 1)
l[:4] = range(100)
l.extend([-2, -7, -8, -1, -0])
del l[:95]
l.__delitem__(0)
l.__delitem__(0)
l.remove(99)
# l[:100] = range(1)
l.sort(key=abs)
# print(abs(-7))
# print(ord('a'))
# print('JjAa'.casefold())
print(l)



# a1 = [1, 's', 2, slice(2, 10)]
# a2 = (1, 's', 2, slice(2, 10))
# print('list size  =', sys.getsizeof(a1))
# print('tuple size =', sys.getsizeof(a2))

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))

# print_matrix(enumerate(l, 3))


