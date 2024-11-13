print('Чтобы выбраться вы должны разгадать загадку')
print('+-----------------------------------------+')
# выводим рандомное число с 3 до 20
print('Выход из ловушки за этими дверями')
print('+-----------------------------------------+')
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
    print('+-----------------------------------------+')
    print('Ты разгадал загадку и вышел из ловушки!')
