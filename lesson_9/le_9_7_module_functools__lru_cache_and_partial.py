from functools import lru_cache, partial

# 1_lru_cache
print('{:-^50}'.format(' exercise 1 '))


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 4):
    print(fibonacci(i))

# 2_partial
print('{:-^50}'.format(' exercise 2 '))


def add(x, y):
    return x + y


add_to_five = partial(add, 5)
print(add_to_five(3))
print(add_to_five(5))


print_with_comma = partial(print, sep=', ', end='\n---\n')
print_with_comma(1, 2, 3)
