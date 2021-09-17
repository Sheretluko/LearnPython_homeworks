# Тема "Функции". Задание 2

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

price_f = format_price(56.24)
print(price_f)