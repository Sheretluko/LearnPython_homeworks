# Напишите функцию hello_user(), которая с помощью функции input()
# спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”.
# Функция hello_user() должна перехватывать KeyboardInterrupt,
# писать пользователю "Пока!" и завершать работу при помощи оператора break

def hello_user():
    answer = ''
    while answer.lower() != 'хорошо':
        try:
            answer = input('Как дела? ')
        except KeyboardInterrupt:
            print('\nПока')
            break

hello_user()