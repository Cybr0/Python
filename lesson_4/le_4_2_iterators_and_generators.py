import random
import time


def fibonacci(count):
    first, second = 0, 1
    for fib in range(count):
        # if fib == 5:
        #     second = None
        yield second
        first, second = second, first + second


def generator_function():
    for x in range(3):
        for y in range(2):
            if x > 0:
                yield y


def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]    end'


'''
ajfkjaksfjkjfkajsfkjafskjfaksfjjjjksajfkjaskfjkfjkfjskajfkjakfjkfajfkjaksfjkjfkajsfkjafskjfaksfjjjjksajfkjaskfjkfjkfjskajfkjakfjkf
'''


def sleep(seconds):
    start = time.time()
    while time.time() - start < seconds:
        yield


def produce(consumer):
    while True:
        yield from sleep(1)
        data = random.randint(1, 100)
        consumer.send(data)


def consume():
    sum_ = 0
    count = 0
    while True:
        data = yield
        print('Got data', data)
        sum_ += data
        count += 1
        print('Sum', sum_)
        print('Average', sum_ / count)
        print()


def main():
    # count = int(input('How many Fibonacci numbers to print?'))
    # for numb in fibonacci(count):
    #     print(numb)

    # generator1 = generator_function()
    # for value in generator1:
    #     print(value)
    # print('#'*50)
    # generator2 = (y for x in range(3) for y in range(2) if x > 0)
    # for value in generator2:
    #     print(value)
    # for value in generator2:
    #     print(value)
    #
    # for value in generator():
    #     print(value)
    consumer = consume()
    next(consumer)

    producer = produce(consumer)
    while True:
        next(producer)





if __name__ == '__main__':
    main()
