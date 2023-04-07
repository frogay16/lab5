from random import randint

a = []
for i in range(50):
    a.append(randint(0,1000))
print("Список:", *a)
print("Повторяющиеся числа:", *set([i for index, i in enumerate(a) if i in a[index + 1:]]))