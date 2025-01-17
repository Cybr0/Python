import sys


class MyManager(object):
    def __init__(self):
        self.resource = 42

    def __enter__(self):
        print('Entered context')
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Left context')
        if exc_type:
            print('(Exception occurred: {})'.format(exc_type))


# with MyManager() as resource:
#     print('Some actions with resource: ', resource)
#     # raise ValueError


def my_with(manager, context_body):
    resource = manager.__enter__()
    exc_type, exc_value, exc_trace_back = None, None, None
    error = None
    try:
        context_body(resource)
    except Exception as exc:
        exc_type, exc_value, exc_trace_back = sys.exc_info()
        error = exc
    finally:
        manager.__exit__(exc_type, exc_value, exc_trace_back)
        if error:
            raise error


def context_body(resource):
    print('Some actions with resource: ', resource)
    # raise ValueError


def main():
    # my_with(MyManager(), context_body)

    # with open(__file__, 'a+') as source:
    #     # for number, line in enumerate(source, 1):
    #     #     print('{:3}| {}'.format(number, line), end='')
    #     source.write('print("saved func")\n')
    pass


if __name__ == '__main__':
    main()

print("saved func")
print("saved func")
