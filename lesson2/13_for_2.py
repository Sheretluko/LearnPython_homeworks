# Тема "Цикл for". Задание 2
# Ввести строку и вывести на экран вертикально:
# один символ на каждой строке

def main():
    line = input('Введите любую строку: ')

    for letter in line:
        print(letter)

main()