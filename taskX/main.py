# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.
#
# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей
# Постарайтесь найти самое оптимальное решение.
import math

num1 = 23436
num2 = 190187200
num3 = 380457890232
num = 0
flag = True

while flag:
    choice_num = int(input(f'Выберите число для нахождения делителей:\n'
                           f'введите 1, чтобы выбрать число {num1},\n'
                           f'введите 2, чтобы выбрать число {num2},\n'
                           f'введите 3, чтобы выбрать число {num3}.\n'))
    if choice_num == 1:
        num = num1
        flag = False
    elif choice_num == 2:
        num = num2
        flag = False
    elif choice_num == 3:
        num = num3
        flag = False
    else:
        print('Вы ввели не верное значение. Принимаются только 1, 2 и 3. Попробуйте еще раз.\n')
print(f'Будем работать с числом {num}')

div_list = []
for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
        div_list.append(i)
        if i != num // i:
            div_list.append(num // i)
div_list.sort()

print(div_list)
