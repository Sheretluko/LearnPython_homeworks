# Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding = 'utf-8') as infile:
    content = infile.read()
    print(f'Количество символов в тексте: {len(content)}')

    words = content.split()
    print(f'Количество слов в тексте: {len(words)}')

    content = content.replace('.', '!')

with open('referat2.txt', 'w', encoding = 'utf-8') as outfile:
    outfile.write(content)