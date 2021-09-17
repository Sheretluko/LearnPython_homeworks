# Тема "Цикл for". Задание 1
# Создать список из десяти целых чисел и
# вывести на экран каждое число, увеличенное на 1.

import random

def main():
    numb_list = [] # Пустой список для добавления случайных чисел
    for num in range(10):
        numb_list.append(random.randint(1, 100))

    for number in numb_list:
        print(number + 1)

main()
