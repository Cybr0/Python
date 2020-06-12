import os
print(os.getcwd())
print(os.walk('try_bootstrap'))

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        index = ' ' * 4 * level
        print(f'{index} C:{os.sep}{os.path.basename(root)}{os.sep}')
        sub_indent = ' ' * 4 * (level+1)
        for file in files:
            print(f'{sub_indent}{file}')

# for files in os.walk('try_bootstrap'):
#     print(files)
# проверка
read_dir('try_bootstrap')