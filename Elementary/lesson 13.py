# a = {1, 2, 3, 4, 5, 6, 7}
# s = list(a)
# s.reverse()
# q = set(s)
# print(q)


# 2
# a = {'красыный','зелоный','синий'}
# s = {'белый','чорный','ак'}
# d = a | s
# print(d)


                    # 3
# q = {1, 2, 3, 4, 5}
# w = {4, 5, 6, 7, 8}
# e = set()
#
# for i in q:
#     if i in w:
#         e.add(i)
#         print(e)




                    # 4
# a = {'алма', 'соок', 'курут', 1, 45, 98}
# s = set()
# for i in a:
#     if type(i) == int or type(i) == float:
#         s.add(i)
#         print(s)











                        #1
# a = {'алма', 'банан', 'алмурут'}
# if 'алма' in a:
#     print('фрукт алма есть в множестве:')
# else:
#     print('фрукт алма нету в множестве:')


                        # 2
# tv = {'Бишкек', 'Нарын', 'Ош'}
# a = {'Талас', 'Кытай'}
# s = tv | a
# if 'Бишкек' in s:
#     print('бар да')
# else:
#     print('жок да')


                        # 3
# a = {1, 2, 3, 4, 5, 6, 7}
# if 1 in a:
#     print('цифра 5 есть в множестве:')
# else:
#     print('цифра 5 нету в множестве:')







# новое


# a = {1}
# s = {2}
# d = {3}
# f = a | d
# print(f)




# menu = {
#     'lagman': 150,
#     'plov': 300,
#     'borsh': 105,
#     'manty': 400
# }
#
# a = menu.pop('borsh')
# # print(menu)
#
#
#
#
#
#
#
#
# # print(menu.keys())
# # print(menu.values())
# # print(menu.items())
# s = menu.setdefault('bech-barmak', 280)
# d = a | s
# print(menu)
































# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#"Заполните анкету"

# Student = {
#     'last_name': 'Aisaev',
#     'first_name': 'Izat'
# }


#                   1 - задача

# a = int(input('сколко учеников в классе:'))
# if a > 18:
#     print('переводили:', a - 18 )
# else:
#     print('все помещаютця:')





#                   3 - задача
# x = float(input('введите первый день (x км):'))
# y = float(input('введите цель (y км):'))
#
# a = 1
# s = x
# while s < y:
#     s *= 1.1
#     a += 1
#     print(f'на {a}-й день пробегь состовит не мене {y} км')








#                   4 - задача
# while True:
#     a = input("Введите пароль: ")
#     if len(a) < 8:
#         print("ошибка: менше 8 слов: ")
#         continue
#
#     if any(a.count(i) > 1 for i in a):
#         print("Ошибка: есть повторяющиеся символы: ")
#         continue
#
#     if not any(i in '123456789' for i in a):
#         print('ошибка: нет цифры: ')
#         continue
#
#     if not any('' for i in a):
#         print('ошибка: нет буквы: ')
#         continue
#
#     if not any(i in '!@#$' for i in a):
#         print('Ошибка: нет символы')
#         continue
#
#     print('пароль принят:')
#     break







#                   5 - задача
# a = int(input('введите цифру 1:'))
# s = int(input('введите цифру 2:'))
# d = input('введите символы (+, -, *, / ):')
# if d == '+':
#     print(a + s)
# elif d == '-':
#     print(a - s)
# elif d == '*':
#     print(a * s)
# elif d == '/':
#     if s != 0:
#         print(a / s)
#     else:
#         print('ошимбка деление на ноль')





#                   6 - задача
# 8 типы даных есть
# 1. int
# 2. float
# 3. str
# 4. bool
# 5. list
# 6. tuple
# 7. dict
# 8. set




                    # 7 - задача


# a = []
#
# while True:
#     s = int(input('введите число (1 - выход): '))
#     if s == 1:
#         break
#     a.append(s)
# print('количиство попыток:', len(a))
#



                    # 8 - задача
# a = {'банан', 'груша', 'яблока'}
# print('множество:', a)
#
# s = {'имя': 'Izat', 'age': 15}
# print('словарь',s)
#
# d = (1, 2, 3)
# print('кортеж:', d)
#
# f = ['ош', 'бишкек', 'нарын']
# print('список',f)


                    # 9 - задача
# cd - чыйдит в рабочий стол
# cd + P + tab = рабочий стол
# ls - показывает все файлы
# mkdir - октрывает папку
# rm -rf = удалает файлы
# pwd - местположение
# cd .. - шаг назад
# touch - октрывает файлы






                    # 10 - задача
# i = 1
# while i <= 5:
#     print('while:', i)
#     i += 1
#
#
#
#               for
#                |

# a = ['банан', 'яблока', 'груша', 'персик']
# for a in a:
#     print('for:', a)










