import Operations
import Note
import Ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = Ui.create_note(number)
    array = Operations.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    Operations.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = Operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = Operations.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = Ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    Operations.write_file(array, 'a')