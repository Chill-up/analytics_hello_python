# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
#  *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

together = int(input('Введите общее кол-во сделанных журавликов:\n'))
katya = int(together / 3 * 2)
petya_and_serega = int(katya / 4) #т.к. по условию у них всегда одинаковое кол-во, сделал одну переменную.

print(f'Вместе сделано {together} журавликов. \nПетя сделал {petya_and_serega}, Катя {katya}, Сережа {petya_and_serega}')