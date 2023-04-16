# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

# number = int(input('Введите число: '))
# res = []
# k = 0
# while number >= 2**k:
#     res.append(str(2**k))
#     k += 1
# print(', '.join(res))

n = int(input("Введите число: "))     # 10
degree = 1
while degree < n:
    print(degree, end=' ')
    degree *= 2