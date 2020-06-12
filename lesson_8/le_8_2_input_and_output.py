import os.path
import io
import random
import array

file_path = os.path.join('le_8_dir', 'simple.txt')
with open(file_path, encoding='utf-8') as txt_file:
    text = [float(value) for value in txt_file if value != '\n' and not value.startswith('#')]
    # print(*text, end='', sep='\n')

with open(file_path, 'r+', encoding='UTF-8') as txt_file:
    text = txt_file.read(6)
    print('r+ =', text)
    print('tell()', txt_file.tell())
    txt = txt_file.read()
    print('txt_file.seek(0)')
    txt_file.seek(0)
    text = txt_file.read(6)
    print('r+ =', text)
    txt = txt_file.read()
    print('==========\ntxt_file.read()\n==========\n', )
    # print('#print()', file=txt_file)
    # txt_file.write('#--written by open--\n')

##############################


# print(os.chdir('le_8_dir'))
buffer_data = io.StringIO('asdf in memory')
print('tell()', buffer_data.tell())
data = buffer_data.read()
print('Data:', data)
data = buffer_data.read()
print('tell()', buffer_data.tell())
if len(data) is 0:
    print('Data: empty')
else:
    print(r'\n{}|'.format(data), len(data), type(data))

print('io.StringIO.getvalue() =', buffer_data.getvalue())
buffer_data.close()

print('\n', '+' * 50)

with open(file_path, 'r+') as file:
    # print(file.tell())
    file.seek(0,
              io.SEEK_CUR)  # не работает с файлами(в режиме append, нужен режим read - тем не менее возникают ошибки)
    # file.write('#test append\n#')

numbers = [random.randint(-1_000_000_000, 1_000_000_000)
           for _ in range(1000)]
with open('le_8_dir/new_file.txt', 'w') as file_txt:
    for number in numbers:
        file_txt.write('{}\n'.format(number))

numbers_array = array.array('i', numbers)
# print(numbers_array)
with open('le_8_dir/new_file.bin', 'wb') as file_bin:
    file_bin.write(numbers_array)
