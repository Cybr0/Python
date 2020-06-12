# from random import randint
# x = randint(1, 1000)
# user_num = 0
# cnt = 0
# while True:
#     user_num = int(input('Я загадал число, - уададай: '))
#     cnt += 1
#     if user_num == x:
#         print(f"Ты удал {x}, количество попыток: {cnt}")
#         break
#     elif user_num > x:
#         print("мое число меньше")
#     else:
#         print("мое число больше")
from datetime import date, datetime, timedelta
import locale
import os.path as path
import os
locale.setlocale(locale.LC_ALL, 'ru')

# # date
# today = date.today()
# print(today)
# print('day = ', today.day)
# print('month = ', today.month)
# print('year = ', today.year)
# print(today.weekday())

# datetime
# now = datetime.now()
# today = datetime.today()
# print(now)
# print(today)
# print(now.hour, ':', now.minute, sep='')

now = datetime.now()
print(now.strftime('%d %h, %a %H:%M %Y'))
print(now.strftime('%x'))
print(now.strftime('%X'))
print("#"*50)
print(now)
print(now + timedelta(days=1, hours=2, minutes=10))
print(now)

print(path)

# os.makedirs('C:/loop')
print(os.name)
print(os.environ)
print(os.listdir('C:/tim/hero'))