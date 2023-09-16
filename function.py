import note
import ui
import file_operation

number = 6

def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if note.Note.get_id(note) == note.Note.get_id(notes):
            note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена.')

def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(note.Note.map_note(notes))
        if text == 'ad':
            logic = False
            print('ID: ' + note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in note.Note.get_date(notes):
                print(note.Note.map_note(notes))
    if logic == True:
        print('Нет заметок!')

def id_edit_del_show(text):
    id = input('Введите id нужной заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == note.Note.get_id(notes):
            logic == False
            if text == 'edit':
                note = ui.create_note(number)
                note.Note.set_title(notes, note.get_title())
                note.Note.set_boby(notes, note.get_body())
                note.Note.get_date(notes)
                print('Заметка изменена.')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена!')
            if text == 'show':
                print(note.Note.map_note(notes))
    if logic == True:
        print ('Такой заметки нет, введите верный id!')
    file_operation.write_file(array, 'a')