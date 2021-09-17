# Тема "Цикл for". Задание 3
# Создать список с оценками разных классов в школе.
# Рассчитать среднюю оценку в школе и среднюю оценку в каждом классе

def main():
    # Список с оценками каждого класса
    school_scores = [
    {'school_class': '5а', 'scores': [3, 4, 3, 5, 4, 5, 3, 2, 4]},
    {'school_class': '5а', 'scores': [2, 4, 3, 5, 4, 4, 3, 2, 4]},
    {'school_class': '5б', 'scores': [3, 4, 3, 5, 4, 5, 3, 3, 5]},
    {'school_class': '6а', 'scores': [4, 5, 4, 3, 4, 3, 3, 2, 5]},
    {'school_class': '6б', 'scores': [5, 3, 5, 5, 5, 5, 3, 4, 4]},
    {'school_class': '6в', 'scores': [5, 2, 3, 4, 2, 3, 3, 4, 5]},
    {'school_class': '7в', 'scores': [3, 4, 2, 3, 4, 3, 4, 4, 3]},
    {'school_class': '7г', 'scores': [3, 4, 3, 3, 5, 5, 3, 2, 4]}
    ]

    average_school = calc_average_school(school_scores)
    print(f'Средняя оценка по школе: {average_school:.2f}')

    calc_average_class(school_scores)

def calc_average_school(school_scores):
    total = 0 # Счетчик для суммирования всех оценок
    amount_scores = 0 # Счетчик для подсчета количества оценок
    for class_scores in school_scores:
        for score in class_scores['scores']:
            total += score
        amount_scores += len(class_scores['scores'])
    
    return total / amount_scores

def calc_average_class(school_scores):
    for class_scores in school_scores:
        total = 0 # Счетчик для суммирования оценок класса
        for score in class_scores['scores']:
            total += score
        average_class = total / len(class_scores['scores'])
        print(f"Средняя оценка {class_scores['school_class']}: {average_class:.2f}")
main()