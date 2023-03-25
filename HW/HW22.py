# Задача 22: ---------------------------------------------------------
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random 

n = int(input("Введите длину первого набора: "))
m = int(input("Введите длину воторого набора: "))
list_1 = []

for i in range(n):
    list_1.append(random.randint(1, 10))
print(list_1)

list_2 = []
for i in range(m):
    list_2.append(random.randint(1, 10))
print(list_2)

first_set = set(list_1)
second_set = set(list_2)

print(first_set)
print(second_set)
print()
common_intersection = first_set.intersection(second_set)

final_list = list(common_intersection)

def Sort_Increase(number_list):  # метод сортировки чисел по возрастанию
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            if number_list[i] > number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
    return number_list


print(Sort_Increase(final_list))
