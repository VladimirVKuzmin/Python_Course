#Задача №25. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2 
# Для решения данной задачи используйте функцию .split()

# my_string = ' a a a b c a a d c d d '
# print(my_string)
# my_string = list(my_string.split())
# print(my_string)
# temp = []
# for i in my_string:
#     if i in temp:
#         print(f'{i}_{temp.count(i)}', end = ' ')
#         temp.append(i)
#     else:
#         print(i, end = ' ')
#         temp.append(i)

import random
import string

my_string = [random.choice(string.digits) for _ in range(30)]
print(my_string)

dict_count = {}
for item in my_string:
    dict_count[item] = dict_count.get(item, -1) + 1
    if dict_count.get(item) > 0:
        print(f'{item}_{dict_count.get(item)}', end=' ')
    else:
        print(item, end=' ')