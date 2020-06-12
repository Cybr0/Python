# file = open('5_path.py', 'r', encoding='UTF8')

# print(file.read(60))
# print(file.encoding)
# file.close()
# lines = ['1_str', '2_str']
# with open('1.txt', 'a', encoding='utf8') as f:
#     f.writelines(f'{i}\n' for i in lines)
#     t = open('1.txt', 'a', encoding='utf8')
#     print(t.write('sss'))

import os

def shower_what_into_dir(dir):
    for root, dir, files in os.walk(dir):
        level = ' ' * 4 * root.count(os.sep)
        print(f'{level} C:{os.sep}..{os.sep}{os.path.basename(root)}{os.sep}')
        level_file = ' ' * 4 * (root.count(os.sep) + 1)
        for file in files:
            print(level_file, file)

shower_what_into_dir(f'try_bootstrap')