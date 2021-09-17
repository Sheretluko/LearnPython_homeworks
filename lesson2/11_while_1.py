# Напишите функцию hello_user(), которая с помощью функции input()
# спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”

def hello_user():
    answer = ''
    while answer.lower() != 'хорошо':
        answer = input('Как дела? ')

hello_user()
