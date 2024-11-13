#рамка вокруг сообщения для пользователя
'''
рекомендация по созданию рамки взята с источника stackoverflow.com
'''
from math import ceil, floor
def boxed_msg(msg):
    lines = msg.split('\n') # разбиваем строку на список строк
    max_length = max([len(line) for line in lines]) # находим максимальную длину строки
    horizontal = '+' + '-' * (max_length + 2) + '+\n' # строка горизонтальной рамки
    res = horizontal
    for l in lines:
        res += format_line(l, max_length) # добавляем к строке горизонтальной рамки строку с выравниванием
    res += horizontal
    return res.strip()

def format_line(line, max_length):
    half_dif = (max_length - len(line)) / 2
    return '| ' + ' ' * ceil(half_dif) + line + ' ' * floor(half_dif) + ' |\n'


print(boxed_msg('Чтобы выбраться вы должны разгадать загадку'))

# выводим рандомное число с 3 до 20
print(boxed_msg('Выход из ловушки за этими дверями'))
print()
import random

n = random.randint(3, 20)
print('На первой скрежали Вам открывается число:', n)


# вычисляем пароль
def this_exit(number):
    pas = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0: # если число делится на i и j без остатка
                pas += str(i) + str(j) # переводим числа в строку
    return pas


result = this_exit(n)
print('На второй скрежали вы вводите число:', result)

print()
print()

if result == this_exit(n):
    print(boxed_msg('Ты разгадал загадку и вышел из ловушки!'))
