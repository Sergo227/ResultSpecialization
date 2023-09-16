import note

def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return note.Note(title=title, body=body)

def menu():
    print("&\n Это программа 'Заметки'. Имеются следующие функции:\n\n1 - вывод всех заметок из файла\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text

def goodbye():
    print('До свидания! \n Быстрее возвращайтесь к нам!')