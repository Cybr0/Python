# import os
# from random import randint as r, shuffle
# print("="*50)
# from w_lib import get_len
# print("="*50)
# import w_lib
# print("="*50)
#
#
# # print(os.getcwd())
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(*l)
# print(r(1,2))
#
# new_list = [n + 2 for n in l if n == 3]
# print(new_list)
#
# print('-' * 50)
# print(w_lib.get_count("holly wood", 'o'))
# print(w_lib.get_len("holly wood"))
# print(get_len("holly wood"))

l1 = [1, 2, 3]
l2 = [i+10 if i != 2 else i for i in l1]
print(l2)

