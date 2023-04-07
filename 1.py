from random import randint

a = []
for i in range(5):
    a.append(randint(-10,10))

n = int(input())

if n in a:
    print('Поздравляю, Вы угадали число!', "Список: ", *a)
else:
    print('Нет такого числа!', "Список: ", *a)
