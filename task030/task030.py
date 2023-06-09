# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input('Введите первый элемент арифметической прогрессии (целое положительное число):\n'))
d = int(input('Введите шаг прогрессии (разность), целое положительное число:\n'))
prog_len = int(input('Введите нужное количество элементов прогрессии, целое положительное число:\n'))

arithmetic_progression = []
for i in range(1, prog_len + 1):
    arithmetic_progression.append(int(first + (i - 1) * d))

print(arithmetic_progression)
