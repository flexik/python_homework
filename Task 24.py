# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 1 3 2 1 1 6
# Output: 8

bushes_qty = int(input('введите кол-во кустов: '))
berries = list(map(int, input(f'введите кол-во ягод на каждом из {bushes_qty} кустов через пробел: ').split()))
result = 0
for i in range(1, bushes_qty-1):  
    if (berries[i]+berries[i+1]+berries[i-1] > result):
        result = berries[i]+berries[i+1]+berries[i-1]
print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль - {result} ягод')
