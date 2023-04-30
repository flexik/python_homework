# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)

array_def = [1, 3, 7, 10, 5, 8]
array_result = []
minimum = int(input('min: '))
maximum = int(input('max: '))
for i in range(len(array_def)):
    if minimum <= array_def[i] <= maximum:
        print(i,f"({array_def[i]})")
        array_result.append(i)
print(f'Индексы искомого диапазона: {array_result}')