# Задача 14 ---------------------------------------------------
# Требуется вывести все целые степени двойки(т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
num = 1
print(1)
for i in range(1, n):
    if(num < n):
        if(num * 2 > n):
            break
        else:
            num = num * 2
            print(num)