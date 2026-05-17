#Приветствие программы и описание её функций.
print ('Добро пожаловать в калькулятор v1.1.1 от AlterWhite \n' \
'В данной версии доступны следующие функции: \n'
'-------------------------------------------------------------- \n' \
'1. Сложение ---> (+) \n' \
'2. Вычитание ---> (-) \n' \
'3. Умножение ---> (*) \n' \
'4. Деление ---> (/) \n' 
'5. Возведение в степень ---> (**) \n'\
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
    elif '**' in quest:
        quest1 = quest.split('**')
        print(int(quest1[0]) ** int(quest1[1]))
    elif '/' in quest:
        quest1 = quest.split('/')
        if quest1[1] == '0':
            print('На 0 делить нельзя!!!')
        else:
            print(int(quest1[0]) / int(quest1[1]))
    elif '*' in quest:
        quest1 = quest.split('*')
        print(int(quest1[0]) * int(quest1[1]))
