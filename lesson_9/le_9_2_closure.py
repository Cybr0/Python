# замыкание
print('{:-^50}'.format(' exercise 1 '))


def add(x):
    def do_add(y):
        return x + y

    return do_add


add_to_five = add(5)
print(add(2)(3))
print(add_to_five(3))
print(add_to_five(10))

# 2
print('{:-^50}'.format(' exercise 2 '))


def make_powers_1(count):
    powers = []
    for i in range(count):
        powers.append(lambda x: x ** i)
    return powers


def make_powers_2(count):
    powers = []
    for i in range(count):
        powers.append((lambda p: lambda x: x ** p)(i))
    return powers


def make_powers_3(count):
    powers = []
    for i in range(count):
        powers.append(lambda x, p=i: x ** p)
    return powers


def make_powers_4(count):
    powers = []
    for i in range(count):
        powers.append(lambda x, i=i: x ** i)
    return powers


powers = make_powers_4(3)
for power in powers:
    print(power(2))


# 3
# in applied code
print('{:-^50}'.format(' exercise 3 '))
handlers = []
for i in range(1, 4):
    def on_click(i=i):
        print('Button {} clicked!'.format(i))
    handlers.append(on_click)

# in event loop
for handler in handlers:
    handler()