# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

userNum = int(input('трёхзначное число: '))

num1 = userNum // 100
num2 = userNum // 10 % 10
num3 = userNum % 10

print(f"Сумма цифр числа {userNum} равна {num1+num2+num3}")