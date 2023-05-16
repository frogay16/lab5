weekdays = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

k = int(input("Сколько выходных дней вы хотите на этой неделе? "))

if k == 1:
    weekends = weekdays[-1]
elif k > 1:
    weekends = weekdays[-k:]

workdays = weekdays[0:7-k]

print('Ваши выходные дни: ', *weekends)
print('Ваши рабочие дни: ', *workdays)