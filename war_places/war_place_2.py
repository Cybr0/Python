from time import time


def sleep(timer):
    now = time()
    while time() - now < timer:
        yield


def produce(consumer_):
    data = 'file_{}.png'
    while True:
        yield from sleep(0.3)
        # consumer.send(data)
        files = consumer_.send(data.format(round(time() * 1_000 - 1590272000000)))
        yield files


def consume():
    files = 0
    while True:
        data = yield files
        print('data:', data)
        files += 1


def another_app_doing():
    while True:
        yield from sleep(1)
        print('-' * 10)
        print('app doing')
        print('-' * 10)


if __name__ == '__main__':
    consumer = consume()
    next(consumer)
    producer = produce(consumer)

    app = another_app_doing()
    time_ = 3
    timer = sleep(time_)
    count_files = 0
    while True:
        count_files = next(producer)
        f_count_files = count_files
        next(app)

        try:
            next(timer)
        except StopIteration:
            print('some_thing_else ----------------->  ', time_)
            print('files now       ----------------->  ', f_count_files)
            timer = sleep(time_)
