# Задача №1 За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750 Output: 2

# n = 700
# m = 750
# def distance(a, x):
#     t = (a + x - 1) // a
#     return t
# print(distance(n,m))

import math

per_day = int(input('ВВедите сколько машина проезжает в день: '))
total_dist = int(input('Сколько машина проедет всего: '))
print(f'Машине потребуется {(total_dist + per_day/per_day -1 )//per_day} Дней')