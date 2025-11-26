import csv

from urllib3.filepost import writer

#
student = [
    ['Name', 'age'],
    ['Argen', 19 ],
    ['Bob', 54 ],
    ['Jiba', 18]
]

# #
# with open('tex.csv', 'w', encoding='utf-8') as f:
#     w = csv.writer(f)
#     w.writerows(student)
# #
#
# s = open('tex.csv', 'r')
# print(s.read())
# s.close()


# with open('tex.csv', encoding='utf-8') as f, \
#      open('r.csv', 'w', encoding='utf-8') as q:
#
#     q.write(f.readline())
#
#     for line in f:
#         age = int(line.split(',')[1])
#
#         if age > 18:
#             q.write(line)
#         elif age <= 18:
#             break
#
#
#




















# ---------------------------------------------------------------------------------------><<>><









































































































































































































#
# filename = "people.csv"
#
# # Читать CSV
# def read_csv():
#     with open(filename, newline='', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             print(row)
#
# # Фильтр: показать людей старше 25
# def filter_age():
#     with open(filename, newline='', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)  # пропускаем заголовок
#         for name, age, city in reader:
#             if int(age) > 25:
#                 print(name, age, city)
# #
# # Добавить нового человека
# def add_person(name, age, city):
#     with open(filename, 'a', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f)
#         writer.writerow([name, age, city])
#     print("Добавлено:", name, age, city)
#
# # Пример
# print("Все данные:")
# read_csv()
#
# print("\nЛюди старше 25:")
# filter_age()
#
# add_person("Алина", 30, "Бишкек")
