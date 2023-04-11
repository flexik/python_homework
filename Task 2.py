# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# 1 Вариант
# print("Введите трехзначное число: ")
# user_number = input()
# a = int(user_number[0])
# b = int(user_number[1])
# c = int(user_number[2])
# print(a + b + c)

# 2 Вариант
print("Введите трехзначное число: ")  # 352
user_number = int(input())
a = user_number % 10                   # 352 % 10 = 2
b = user_number % 100 // 10            # 352 % 100 = 52 // 10 = 5
c = user_number // 100                 # 352 // 100 = 3
print(a + b + c)