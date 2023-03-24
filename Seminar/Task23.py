#Задача №23. Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

# f = [-1, 0, -1, 5, 2, 3, 10, 10, 5]
# l = 0
# for i in range(0, len(f)-1):
#     if f[i] < f[i+1]:
#         l += 1

# print(f)
# print()
# print(l)

import random

# my_list = [random.randint(0, 10) for i in range(10)]
# count = 0
# for i in range(0, len(my_list)-1):
#     if my_list[i] < my_list[i+1]:
#         count += 1

# print(my_list)
# print()
# print(count)

my_list = [random.randint(0, 10) for i in range(10)]
count = 0
for i in range(1, len(my_list)):
     if my_list[i] > my_list[i-1]:
         count += 1

print(my_list)
print()
print(count)