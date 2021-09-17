# Напишите функцию ask_user() которая с помощью функции input()
# просит пользователя ввести вопрос, а затем, если вопрос есть
# в словаре, программа давала ему соотвествующий ответ.

def main():
    answer_dict = {
        "Как дела?": "Хорошо!",
        "Что делаешь?": "Программирую.",
        "Как настроение?": "Отличное.",
        "Какие планы?": "Можно отдохнуть.",
        "Когда закончишь?": "Скоро.",
        "Пошли?": "Еще не закончил.",
        "Скажешь что-нибудь?": "Самое время.",
        }

    ask_user(answer_dict)

def ask_user(answer_dict):
    while True:
        question = input('Ваш вопрос: ')
        if question in answer_dict:
            print(f'Программа: {answer_dict[question]}')
        elif question.lower() == 'нет' or question.lower() == 'не хочу':
            print('Хорошо.')
            break
        else:
            print('Не знаю.')

main()