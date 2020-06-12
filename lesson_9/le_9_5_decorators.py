def decorator(fn):
    def decorated_fn(*args, **kwargs):
        print('Starting decorated function')
        fn(*args, **kwargs)
        print('End of decorated function')

    return decorated_fn


def make_decorator(string):
    def decorator_(fn):
        def decorated_fn(*args, **kwargs):
            print(string)
            fn(*args, **kwargs)

        return decorated_fn

    return decorator_


def main():
    # 1
    # def print_hello():
    #     print('Hello!')
    # print_hello = decorator(print_hello)
    # print_hello()

    # 2
    # @decorator
    # def print_hello():
    #     print('Hello!')
    #
    # print_hello()

    # 3
    @make_decorator('Before invocation')
    @make_decorator('Another decorator')
    def print_hello():
        print('Hello!')

    print_hello()


if __name__ == '__main__':
    main()
