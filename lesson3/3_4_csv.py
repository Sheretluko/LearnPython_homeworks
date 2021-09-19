# Создайте список словарей:
from typing import ClassVar


[
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
# Запишите содержимое списка словарей в файл в формате csv

import csv

staff = [
{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
with open('export.csv', 'w', encoding = 'utf-8') as outfile:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(outfile, fields, delimiter = ';')
    writer.writeheader()
    for user in staff:
        writer.writerow(user)