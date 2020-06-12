from itertools import product, chain
from itertools import permutations, \
    combinations, \
    combinations_with_replacement
from itertools import takewhile, dropwhile

# for i in range(1, 5):
#     for j in range(1, 5):
#         print('{} x {} = {}'.format(i, j, i*j))

# этот же пример с product(объединяет 2 последовательности)
for i, j in product(range(1, 5), range(1, 5)):
    # print('{} x {} = {}'.format(i, j, i * j))
    pass

# chain склеивает 2++ итеротора(возвращает значения из одного, после из другого)
for i in chain(range(1, 5), range(5, 10), range(10, 15)):
    # print(i)
    pass

# permutations, combinations, combinations_with_replacement
string = 'ABC'
elements = 2
if False:
    print(list(permutations(string, elements)))
    print(list(combinations(string, elements)))
    print(list(combinations_with_replacement(string, elements)))

# takewhile, dropwhile
values = [1, 4, 3, 5, 3, 2, 8]
predicate = lambda x: x < 5

for elem in takewhile(predicate, values):
    print(elem)
print('---------')
for elem in dropwhile(predicate, values):
    print(elem)

