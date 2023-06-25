import Note


def create_note(number):
    title = check_len_text_input(
        input('Enter note name: '), number)
    body = check_len_text_input(
        input('Enter note description: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nThis is Note. I can to this:\n\n1 - Output all notes\n2 - Add note\n3 - Del note\n4 - Edit note\n5 - Chouse note by date\n6 - Show note by id\n7 - Exit\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("See ya")