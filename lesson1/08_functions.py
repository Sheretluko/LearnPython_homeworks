# Тема "Функции". Задание 1
# Ввести две строки и создать функцию, соединяющую их
# с помощью символа "&"

def get_summ(one, two, delimeter):
    summ = one+delimeter+two
    print(summ.upper())

string1 = 'Learn'
string2 = 'Python'
summ = get_summ(string1, string2, delimeter = '&')