# Задачи из курса Geekbrains Основы Python для аналитиков (и тестировщиков) 

## Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

```doctest
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
```

## Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

```doctest
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
```

## Задача 6: Счастливый билет
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 

Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

```doctest
385916 -> yes
123456 -> no
```

## Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек.
Разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

```doctest
3 2 4 -> yes
3 2 1 -> no
```

## # Задача 10: Перевернуть монетки
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 

Выведите минимальное количество монет, которые нужно перевернуть.

```doctest
5 -> 1 0 1 1 0 
2
```

## Задача 12: Отгадать числа по их сумме и произведению
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.

Помогите Кате отгадать задуманные Петей числа.

## Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
```doctest
10 -> 1 2 4 8
```

## Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*
``` doctest
Введите длину массива (целое число):
10
Введите число, количество которых нужно посчитать в массиве:
2
Дан массив целых чисел:
[1, 3, 0, 0, 0, 2, 3, 2, 0, 1]
Количество вхождений числа 2 в массив = 2
```

## Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

```doctest
Введите длину массива (целое число):
10
Введите число, к которому будем искать наиболее близкий элемент:
10
Дан массив целых чисел:
[93, 69, 37, 100, 23, 21, 18, 89, 33, 16]
Наиболее близкое к 10 число в массиве это 16

```

## Задача 20: Подсчет очков в настольной игре Скрабл (Scrabble) 
Каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:

A, E, I, O, U, L, N, S, T, R – 1 очко; 

D, G – 2 очка; 

B, C, M, P – 3 очка; 

F, H, V, W, Y – 4 очка; 

K – 5 очков; 

J, X – 8 очков; 

Q, Z – 10 очков. 

А русские буквы оцениваются так: 

А, В, Е, И, Н, О, Р, С, Т – 1 очко; 

Д, К, Л, М, П, У – 2 очка; 

Б, Г, Ё, Ь, Я – 3 очка; 

Й, Ы – 4 очка; 

Ж, З, Х, Ц, Ч – 5 очков; 

Ш, Э, Ю – 8 очков; 

Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

```doctest
ноутбук
    12
```

## Задача 22. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа.

n — кол-во элементов первого множества.

m — кол-во элементов второго множества.

Затем пользователь вводит сами элементы множеств.

```doctest
Первый массив:
[4, 6, 7, 7, 7, 2]
Второй массив:
[3, 4, 7, 2, 6, 5]
Числа, которые встречаются в обоих наборах без повторений:
[2, 4, 6, 7]
```

## Задача 24. В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 

Таким образом, у каждого куста есть ровно два соседних.

Всего на грядке растёт N кустов.

Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
на i-ом кусте выросло ai ягод.

В этом фермерском хозяйстве внедрена система автоматического сбора черники.

Эта система состоит из управляющего модуля и нескольких собирающих модулей.

Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.

```doctest
Пример

Сгенерирована грядка: [89, 48, 52, 94, 27, 47]
Для сбора выбран куст по индексу 5, его значение = 47
С куста по индексу 5 и 2 его соседей (слева и справа) собрано 163 ягод
```

## Задача 26: Напишите программу, которая, возводит число А в целую степень B с помощью рекурсии.

```doctest
Введите первое целое положительное число:
3
Введите второе целое положительное число:
5
243
```

## Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
 Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
``` doctest
Введите первое целое положительное число:
15
Введите второе целое положительное число:
9
24
```

## Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.

Формула для получения n-го члена прогрессии: 

an = a1 + (n-1) * d.

Каждое число вводится с новой строки.

*Пример:*

```doctest
Введите первый элемент арифметической прогрессии (целое положительное число):
3
Введите шаг прогрессии (разность), целое положительное число:
2
Введите нужное количество элементов прогрессии, целое положительное число:
10

[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
```