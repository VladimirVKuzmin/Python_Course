# Задача 10 ----------------------------------------
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и
# той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input()) 
#     if x == 0:
#         count_zero += 1 
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else: print(count_one)

n = int(input('Введите количество монеток: '))
count1 = 0
count2 = 0
print('Вводите 1 или 0: ')
for i in range(n):
    temp = int(input())
    if temp == 0:
        count1 += 1
    if temp == 1:
        count2 += 1
if count1 > count2:
    res = count2
else:
    res = count1
print(f'Результат: {res}')