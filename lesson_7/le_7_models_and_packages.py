import sys
from time import time
import os.path
# from le_7_package import *
from le_7_package import module_2, module
import le_7_package
from le_7_package import pack_func

# [print(attr) for attr in sys.argv if attr != sys.argv[0]]


def sleep(timer):
    start = time()
    while time() - start < timer:
        yield


def argv_hello(text, timer):
    count = 1
    while True:
        yield from sleep(timer)
        print(f'№{count} {text}')
        count += 1


def main():
    print('start')
    if len(sys.argv) >= 3:
        if sys.argv[2].isdigit():
            timer = int(sys.argv[2])
            text = sys.argv[1]
            hello = argv_hello(text, timer)
            while True:
                next(hello)
    print('end')
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # parent_path = os.path.dirname(current_path)
    # module_path = os.path.join(parent_path, 'module')
    # print(os.path.abspath(__file__))
    # print(module_path)
    # sys.path.append(module_path)
    # print(sys.path)

    # le_7_package.module.module_1_func()
    # print(le_7_package.__all__)
    # print(module.module_1_func())
    # print(le_7_package.module.module_1_func())
    print(module.module_1_func())
    print(module_2.module_2_func())
    print(le_7_package.pack_func())
    pack_func()



if __name__ == '__main__':
    main()
