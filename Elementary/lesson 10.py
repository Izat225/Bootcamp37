# while True:
#     a = input('пароль: ')
#     if a == 'Payton123':
#         print('верный пароль')
#         break
#     else:
#         print('не верный пароль')


# while True:
#     s = input('ok: ')
#     print(len(s))



# for i in range (1, 20):
#     if i % 2 == 0 :
#         print(i)





# while True:
#     a = input('пароль: ')
#     if a == 'q':
#         break


                    # 1-hom   1 варианд

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









                                # 1-hom  2 варианд

# while True:
#     parol = input('пароль:')
#     if len(parol) < 8:
#         print("короткий")
#         continue
#     if '123' in parol or 'adc' in parol or 'adc' in parol:
#         print('нельзя повторять: !')
#         continue
#     if not any(parol.isdigit() for parol in parol):
#         print('ошибка нет цифр')
#         continue
#     if not any(parol.isalpha() for parol in parol):
#         print('ошибка нет букв')
#         continue
#     if not any( not parol.isalnum() for parol in parol):






