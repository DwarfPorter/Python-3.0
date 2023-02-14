# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


num = input()
sum_digits = 0

power = len(num) - 2
num = float(num)
num *= int(10 ** power)

while num:
    sum_digits *= int(num % 10)
    num //= 10

    print(int(sum_digits))


# второй способ

print(sum(map(int, list(input ('Введите число').replace(".", "")))))