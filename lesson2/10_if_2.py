# Тема "Цикл if". Задание 2
# Принимает две строки и проверяя их на соответствие условию,
# выводит разные цифры

def main():
    line1 = 'Учи Python, это важно.'
    line2 = 'learn'

    determine(line1, line2)

def determine(line1, line2):
    if not isinstance(line1, str) or not isinstance(line2, str):
        print('0')
    elif line1 == line2:
        print('1')
    elif len(line1) > len(line2):
        print('2')
    elif line2 == 'learn':
        print('3')
    else:
        print('Ничего из перечисленного')
    
main()