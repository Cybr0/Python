from .module import module_1_func
__all__ = ['module']


def wrapper(func):
    def inner_func():
        print('BEGIN decorator')
        func()
        print('END decorator')
    return inner_func


# wrapper(module_1_func)
# module_1_func()


@wrapper
def pack_func():
    print("used le_7_package's func: --> def pack_func()")
    return 1
