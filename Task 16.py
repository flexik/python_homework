# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# Вариант 1 создания масссива с ручным заполнением:
# arr_length = int(input('Введите количество чисел в массиве: '))
# array_numbers = [int(input('Введите натуральное число: ')) for i in range(arr_length)]  
# print(array_numbers)


# Вариант 2 создания масссива с автоматическим заполнением:
arr_length = int(input("Введите число - количество элементов в массиве: "))    
array_numbers = list(range(1, arr_length + 1))  # создание массива чисел с автоматическим заполнением
print(array_numbers)

x = int(input("Введите проверочное число: "))    
count_x = 0
for i in range(1, len(array_numbers)):
    if array_numbers[i] == x:
        count_x +=1
print(f"Число {x} встречается в массиве {count_x} раз")
