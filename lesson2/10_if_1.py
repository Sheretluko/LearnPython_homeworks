# Тема "Цикл if". Задание 1
# Пользователь вводит свой возраст, в ответ функция определяет
# чем ему заниматься

def determine_user(age):
    if age <= 7:
        print('В детский сад.')
    elif age <= 10:
        print('В начальную школу.')
    elif age <= 16:
        print('В среднюю школу.')
    else:
        print('На работу.')

age = int(input('Введите ваш возраст: '))
determine_user(age)