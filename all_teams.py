from random import randint
from team import *

teams_names = ["Грозные Медведи", "Неудержимые Львы", "Пылающие Драконы", "Сверкающие Звезды", "Бесконечные Волки", "Могучие Орлы", "Тайные Пантеры", "Сокрушительные Грифоны", "Пламенные Фениксы", "Неиссякаемые Водовороты", "Ледяные Варвары", "Гремучие Кобры", "Вечные Циклоны", "Невидимые Призраки", "Сияющие Единороги", "Золотые Рыцари", "Трескучие Черепахи", "Хитрые Лисы", "Скалящиеся Йети", "Мрачные Вороны", "Роковые Куклы", "Штормовые Пегасы", "Ревущие Мотыльки", "Искрящиеся Жемчужины", "Мозаичные Пираньи", "Космические Альфы", "Стальные Пумы", "Пыльные Скорпионы", "Исконные Буйволы", "Благородные Змеи", "Светоносные Демоны", "Мифические Ежи", "Хищные Химеры", "Огненные Совы", "Виртуозные Акулы", "Мародерские Гиппогрифы", "Вспышечные Жар-птицы", "Переливающиеся Змеи Горынычи", "Вечные Искатели", "Магические Кентавры", "Мерцающие Радужные Летучие Мыши", "Прозрачные Призраки", "Подземные Драконы", "Живые Статуи", "Блуждающие Лунатики", "Скрытые Гоблины", "Солнечные Фениксы", "Горячие Вулканы", "Галактические Звездные Путники", "Ураганные Ветры"]

def set_teams():
    list_of_teams = []
    for _ in range(5):
        team = TEAM(teams_names[randint(0, len(teams_names) - 1)])
        team.generate_team()
        list_of_teams.append(team)
    return list_of_teams
        
def print_all_available_teams(list_of_teams):
    print("Выберите команду")
    count = 1
    for i in list_of_teams:
        print(f"Команда {count}")
        i.print_team_statistic()
        count += 1



