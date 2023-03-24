# Задача №19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input:   [1, 2, 3, 4, 5] 
# k = 3 Output:  [4, 5, 1, 2, 3]

# n = 2
# m = [1, 2, 3, 4, 5]
# print(m)
# for i in range(0, n):
#     m.insert(0, m[-1])
#     m.pop(-1)

# print(f'{m} -> сдвиг на {n} элемента(ов)')
# print()

# #2
# my_list = [i for i in range(10)]
# print(my_list)

# shift = int(input('На ссколько двигаем вправо: '))
# for i in range(shift):
#     temp = my_list.pop(len(my_list) - 1)
#     my_list.insert(0, temp)

# print(my_list)

# #3
# my_list = [i for i in range(10)]
# print(my_list)

# shift = int(input('На ссколько двигаем вправо: '))

# print(my_list[-shift:] + my_list[:-shift])


#4 
# list_1 = [1, 2, 3, 4, 5]
# list_2 = [0, 0, 0, 0, 0]
# k = 3
# for i in range(len(list_1)):
#     new_pos = (i + k -1) % len(list_1)
#     list_2[new_pos] = list_1[i]

# print(f'{list_1} -> {list_2}')

#5
my_list = [i for i in range(10)]
print(my_list)
new_list = []

shift = int(input('На ссколько двигаем вправо: '))

for i in range(len(my_list)):
    new_list.append(my_list[(i-shift)])
print(new_list)

