# Перепишите функцию 'discounted(price, discount, max_discount=20)'
# из урока про функции так, чтобы она перехватывала исключения,
# когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу
# при помощи float(), а третий - к целому при помощи int() и
# перехватывать исключения ValueError и TypeError,
# если приведение типов не сработало.

def discounted(price, discount, max_discount=20):
    try:
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = int(abs(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        return 'Ошибка при вводе данных.'
    except TypeError:
        return 'Ошибка при вводе данных.'

print(discounted(1000, 6, 3))
print(discounted(1000, 6))
print(discounted('1000', 6, 3))
print(discounted(1000, '6', 3))
print(discounted(1000, 6, 'a'))

