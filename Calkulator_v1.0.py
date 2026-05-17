#Добавление нужных библиотек.
import math

#Приветствие программы и описание её функций.
print ('Добро пожаловать в калькултор v1.0 от AlterWhite \n' \
'В данной версии доступны следующие функции: \n'
'-------------------------------------------------------------- \n' \
'1. Сложение ---> (+) \n' \
'2. Вычитание ---> (-) \n' \
'3. Умножение ---> (*) \n' \
'4. Деление ---> (/) \n' \
'Данная версия работает только с двумя переменными \n'
'-------------------------------------------------------------- \n' \
'Для выхода из программы напиши ---> Стоп')
while True:
    quest = input ('Введите ваше выражение: \n')
    if quest == 'Стоп':
        break
    if '+' in quest:
        quest1 = quest.split('+')
        print(int(quest1[0]) + int(quest1[1]))
    elif '-' in quest:
        quest1 = quest.split('-')
        print(int(quest1[0]) - int(quest1[1]))
    elif '*' in quest:
        quest1 = quest.split('*')
        print(int(quest1[0]) * int(quest1[1]))
    elif '/' in quest:
        quest1 = quest.split('/')
        if quest1[1] == 0:
            print('На 0 делить нельзя!!!')
        else:
            print(int(quest1[0]) / int(quest1[1]))
