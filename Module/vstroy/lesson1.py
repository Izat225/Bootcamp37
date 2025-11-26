# "Ввстроенные модули"

from datetime import datetime, timedelta, tzinfo, time, timezone, date
import datetime

import random
from os.path import split

# now = datetime.now()
#
# america = datetime.strftime(now, '%d:%m:%Y: %p')
# print(america)





# ------------------------------------------------------------
#                          2-ex

#
# date = input('Введите первую дату (ДД.ММ.ГГГГ):')
# date2 = input('Введите вторую дату (ДД.ММ.ГГГГ):')
#
# if date < date2:
#     print('ранше: {date}')
# elif date2 < date:
#     print('ранше: date2')
# else:
#     print('ровны:')

#                        5-ex



# now = datetime.now()
#
# nex = now.replace(day=1)
#
# if nex .month == 12:
#     nex = nex.replace(year=nex.year + 1, month=1)
#
# else:
#     nex = nex.replace(month=nex.month + 1)
#
# mon = nex
#
# while mon.weekday() != 0:
#     mon += timedelta(days=1)

# while mon.month == nex.month:
#     print(mon.strftime('%d, %m, %Y'))
#     mon += timedelta(days=7)

#                       3-ex

# def func(d1, d2):
#
#     date1 = datetime.strptime(d1, "%Y-%m-%d")
#     date2 = datetime.strptime(d2, "%Y-%m-%d")
#
#     difference = (date2 - date1).days
#
#     return difference
#
# d1 = "2025-11-9"
# d2 = "2025-11-10"
# print(func(d1, d2))



#                       6-ex



# birthdays = {
#     "Иван": "11-01",
#     "Мария": "11-02",
#     "izat": "11-11",
# }
#
#
# def a_birthday():
#     today= datetime.date.today().strftime("%m-%d")
#
#     for name, birthday in birthdays.items():
#         if today == birthday:
#             print(f"Сегодня день рождения у {name}!")
#
#
#
# a_birthday()




#                          7-ex


# booked_dates = ["11-01", "11-03", "11-05", "11-11"]
#
# def no(date):
#     if date in booked_dates:
#         print(f"Дата {date} уже занята.")
#     else:
#         print(f"Дата {date} свободна для бронирования.")
#
# no("11-02")
# no("11-03")
# no("11-11")
# #






#                           3-ex
#
# print(random.randint(1, 6))
#
#
#
#
#
#
#                          4-ex
#
# print(random.choice("python"))
#
#
#
#                         5-ex
#
# students = ["Аскат", "Динара", "Айбек", "Султан", "Жарқын"]
# print(random.choice(students))
#
#
#
#                         6-ex
#
# print(random.sample(range(1, 50), 6))
#
#
#
#                         7-ex
#
# nums = [1, 2, 3, 4, 5]
# random.shuffle(nums)
# print(nums)
#
#
#                         8-ex
#
# symbols = 'sdfasdJHJGYBHG0123456789@#$%&'
# password = "".join(random.choice(symbols) for _ in range(8))
# print(password)
#
#
#
#
#                        9-ex
#
# t = 'Python is fun and powerful'
# print(random.choice(t.split()))

































