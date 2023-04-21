# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
import random

n = int(input('Введите длину массива (целое число):\n'))
find = int(input('Введите число, количество которых нужно посчитать в массиве:\n'))
intArray = [random.randint(0, 4) for i in range(n)]
x = 0
print(f'Дан массив целых чисел:\n{intArray}')

#простой способ
# print(f'Количество вхождений числа {find} в массив = {intArray.count(find)}')

#через цикл
for i in range(len(intArray)):
    if intArray[i] == find:
        x += 1

print(f'Количество вхождений числа {find} в массив = {x}')
