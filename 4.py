import random

gr1 = ['Иванов', 'Цветаев', 'Лебедев', 'Соболев', 'Воскресенский', 'Громов', 'Серебрянский', 'Алмазов', 'Корольков', 'Державин']
gr2 = ['Адмиралов', 'Воронцов', 'Золотарев', 'Александров', 'Щедрый', 'Бестужев', 'Гончаров', 'Попов','Иванов','Семенов']


team = random.sample(gr1, 5) + random.sample(gr2, 5)
team = sorted(team)

print("Первая группа:", *gr1)
print("Вторая группа:", *gr2)
print("Команда:", *team)

print("Длина команды:", len(team))


if "Иванов" in team:
    print("Иванов входит в команду")
    count = team.count("Иванов")
    print("Количество студентов c такой фамилией в команде:", count)
else:
    print("Студент Иванов не входит в команду")
