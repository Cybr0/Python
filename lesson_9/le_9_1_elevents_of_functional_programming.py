operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': pow,
}

try:
    first = float(input('Enter first number: '))
    operation = input('Enter operation: ')
    second = float(input('Enter second number: '))
    result = operations[operation](first, second)
except ValueError:
    print('Incorrect input')
except KeyError:
    print('Unsupported operation')
except ZeroDivisionError:
    print('Division by zero')
else:
    print(result)
