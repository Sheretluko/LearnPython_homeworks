# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import datetime, date, time, timedelta
dt_now = datetime.now()
print(f"Сегодня: {dt_now.strftime('%d.%m.%Y')}")
print(f"Вчера: {(dt_now - timedelta(days = 1)).strftime('%d.%m.%Y')}")
print(f"30 дней назад: {(dt_now - timedelta(days = 30)).strftime('%d.%m.%Y')}")

date_before = '01/01/25 12:10:03.234567'
date_after = datetime.strptime(date_before, '%m/%d/%y %H:%M:%S.%f')
print(date_before)
print(date_after)
