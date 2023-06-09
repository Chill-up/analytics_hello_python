# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
import random

n = random.randint(2, 20)
monets = [random.randint(0, 1) for i in range(n)] #генерируем список через list comprehensions
print('На столе лежит следующий набор монет:')
print(monets)
print('0 - орел, 1 - решка')
zeros = monets.count(0)
ones = monets.count(1)

if zeros < ones:
    print(f'Орлов меньше, нужно перевернуть всего {zeros} монет\n')
else:
    print(f'Решек меньше, нужно перевернуть всего {ones} монет\n')
