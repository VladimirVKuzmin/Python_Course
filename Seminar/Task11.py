# Задача №11
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число - 1.

# Input:   5
# Output:  6

#num_fb = int(input('Введите число фибоначчи: '))


# def fibonache(n):
#     # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 каждое число фибоначчи
#     # 1  2  2  4  5  6  7  8   9   10  11  12  13   14   15  порядковый номер числа фибоначчи
#     if n == 0:
#         return 1
#     if n == 1:
#         return 2
#     number0 = 0
#     number1 = 1
#     count = 2
#     while n >= number1:
#         if n == number1:
#             return count
#         temp = number1
#         number1 += number0
#         number0 = temp
#         count += 1
#     return -1
# print(
#     f'Порядковый номер в системе Фибоначчи числа {num_fb} равен {fibonache(num_fb)}')

# n = int(input('Введите число: '))
# n1 = 0
# n2 = 1
# a = 2
# while True:
#     sum = n1 + n2
#     n1 = n2
#     n2 = sum
#     a += 1
#     if sum == n:
#         print(a)
#         break
#     elif sum > n:
#         print(-1)
#         break

# x = int(input('Введите искомое число Фибоначчи: '))

# fib_prev = 0
# fib_curr = 1
# n = 1

# while fib_curr < x:
#     fib_next = fib_prev + fib_curr
#     fib_prev = fib_curr
#     fib_curr = fib_next
#     n += 1
# if fib_curr == x:
#     print(n)
# else:
#     print(-1)

number = int(input('Введите число: '))

fibo_1, fibo_2, index = 0, 1, 1

while fibo_2 < number:
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    index += 1

if fibo_2 == number:
    print(index)
else:
    print(-1)

