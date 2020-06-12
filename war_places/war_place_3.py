import array
import os.path
l = ['qwerty', 'asdfg', 'zxcvb']

for a, b in enumerate(l, 1000):
    # print(a, b)
    pass

with open('le_8_dir/new_file.txt') as file_txt:
    numbers = [int(number) for number in file_txt]

print(numbers)

filename = 'le_8_dir/new_file.bin'
filesize = os.path.getsize(filename)
count = filesize // array.array('i').itemsize
numbers_bin = array.array('i', (0 for _ in range(count)))

print(filesize)
print(count)

with open(filename, 'rb') as file_bin:
    file_bin.readinto(numbers_bin)

print(numbers_bin.tolist())
