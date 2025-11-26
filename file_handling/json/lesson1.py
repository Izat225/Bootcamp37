import json
#
# key = {
#     'password': 'bootcamp37'
# }
#
# with open('security.json', 'w') as password:
#     json.dump(key, password, indent=4)
#
# with open('security.json', 'r') as f:
#     r = json.load(f), ['password']
#
#     a = input('parol:')
#     if a == r:
#         print('yes')
#
#     else:
#         print('no')




#
#
# def load_books():
#     try:
#         with open('books.json', 'r', encoding='utf-8') as q:
#             return  json.load(q)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []
#
#
# def save_books(books):
#     with open('books.json', 'w', encoding='utf-8') as w:
#         json.dump(books, w, ensure_ascii=False, indent=4)
#
#
# def add_books(books):
#     title = input('Введите название книги:')
#     author = input('Введите автора:')
#     year = input('Введите год вупуска:')
#     books.append({'title': title, 'author': author, 'year': year})
#     save_books(books)
#     print('Книга добавлен:')
#
#
# def remove_book(books):
#     title = input('Введите название книги для удаление:')
#     for book in books:
#         if book['title'].lower() == title.lower():
#             books.remove(book)
#             save_books(books)
#             print('Книга удалено')
#             return
#         print('Книга не найден')
#
#
# def search_book(books):
#     keyword = input('Введите название или автора дл поеска:').lower()
#     found = [book for book in books if keyword in book['title'].lower() or keyword in book['author'].lower()]
#     if found:
#         for book in found:
#             print(f'{book['title']} - {book['author']} ({book['year']})')
#     else:
#         print('Книга не найден.')
#
#
#
# #
# def sort_books(books):
#     key = input('Сортироват по ("title/author/year"):').lower()
#     if key in ['title', 'author', 'year']:
#         sorted_books = sorted(books, key=lambda x: x[key])
#         for book in sorted_books:
#             print(f'{book["title"]} - {book['author']} {book['year']})')
#     else:
#         print('Некорректный параметр сортировки')
#
#
# def edit_book(books):
#     title = input('Введите название криги для редиктировки:')
#     for book in books:
#         if book['title'].lower() == title.lower():
#             print('Оставьте поле пустым, если не хотите менять значение')
#             new_title = input('Новое название:') or book['title']
#             new_author = input('Нщвый автор:') or book['author']
#             new_year = input('Новый год:') or book['year']
#             book.update({'title': new_title, 'author': new_author, 'year': new_year})
#             save_books(books)
#             print('Информция обновлен')
#             return
#         print("Книга найден")
#
#
# def main():
#     books = load_books()
#     while True:
#         print('\nМеню:')
#         print('1 — Добавить книгу')
#         print('2 — Удалить книгу')
#         print('3 — Найти книгу')
#         print('4 — Показать все книги')
#         print('5 — Сортировать книги')
#         print('6 — Редактировать книгу')
#         print('0 — Выйти')
#
#         choice = input('Выберите дуйстиве:')
#         if choice == '1':
#             add_books(books)
#         elif choice == '2':
#             remove_book(books)
#         elif choice == '3':
#             search_book(books)
#         elif choice == '4':
#             for book in books:
#                 print(f'{book['title']} - {book['author']} ({book['year']})')
#         elif choice == '5':
#             sort_books(books)
#         elif choice == '6':
#             edit_book(books)
#         elif choice == '0':
#             print('Выход из програмы')
#             break
#
#         else:
#             print('Ошибка: выберите пункт из меню:?')
# #
# if __name__ == "__main__":
#     main()





