# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.
# Например:
# 4 4 5 3 7 2 
# 5 2 3 1 6 3 
# -> [2, 3, 5]

## Первый метод 

# n = int(input('Введите кол-во элементов первого набора целых чисел: ')) 
# m = int(input('Введите кол-во элементов второго набора целых чисел: ')) 

# numbers1 = list(range(n))  # Список №1. Создание первого списка чисел от 0 до заданного числа
# for i in numbers1:         # заполнение первого списка чисел заданных пользователем
#     x = int(input('Введите целое число для первого списка: '))
#     numbers1[i] = x
# print(numbers1)   # проверочный вывод списка чисел на экран 
 
# numbers2 = list(range(m))  # Список №2
# for i in numbers2:         
#     x = int(input('Введите целое число для второго списка: '))
#     numbers2[i] = x
# print(numbers2)

# numbers1 = set(numbers1)   # преобразование созданного списка в множество
# numbers2 = set(numbers2)

# final_numbers = sorted(numbers1.intersection(numbers2))  # нахождение пересечения множеств и создание финального отсортированного множества
# print(f'Числа в порядке возрастания, которые встречаются в обоих наборах : {final_numbers}')


## Второй метод

a = int(input('введи кол-во элементов первого множества: '))
b = int(input('введи кол-во элементов второго множества: '))
spisok_1 = set(map(int, input(f'введите {a} цифр(ы) через пробел: ').split()))
spisok_2 = set(map(int, input(f'введите {b} цифр(ы) через пробел: ').split()))
spisok_3 = sorted(spisok_1.intersection(spisok_2))
print(f'Числа в порядке возрастания, которые встречаются в обоих наборах : {spisok_3}')