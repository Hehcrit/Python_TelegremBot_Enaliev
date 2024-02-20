from os import path, remove, listdir

#создание заметки
def build_note(note_text, note_name):
    with open(f"{note_name}.txt", mode = 'w', encoding= 'utf-8') as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")


def create_note():
    note_name = input("Введите название заметки: ")
    if (path.isfile(f'{note_name}.txt')):
        print("Такое название заметки уже существует")
        create_note()
    else:
        note_text = input("Введите текст заметки: ")
        build_note(note_text, note_name)


def read_note():
    note_name = input("Введите название заметки: ")
    if (path.isfile(f'{note_name}.txt')):
        with open(f"{note_name}.txt", mode='r', encoding='utf-8') as file:
            print(file.read())
    else:
        print("Заметка не найдена")

def edit_note():
    note_name = input("Введите название заметки: ")
    if (path.isfile(f'{note_name}.txt')):
        with open(f"{note_name}.txt", encoding='utf-8') as file:
            r = open(f'{note_name}.txt', mode ='r',  encoding='utf-8')
            print(r.read())
            w = open(f'{note_name}.txt', mode ='w',  encoding='utf-8')
            note_text = input("Введите новый текст заметки: ")
            w.write(note_text)
    else:
        print("Заметка не найдена")


def delete_note():
    note_name = input("Введите название заметки: ")
    if (path.isfile(f'{note_name}.txt')):
        remove(f'{note_name}.txt')
        print("Заметка успешно удалена")
    else:
        print("Заметка не найдена")


def display_notes():            #TASK 4, Показывать список всех заметок
    notes = [note for note in listdir() if note.endswith(".txt")]
    for i in sorted(notes, key=len):
        print(i[:-4])

def main():
    print("Введите NEW NOTE если вы хотите записать новую заметку"
                    "\nКоманда READ NOTE выводит содержимое вашей заметки,"
                    "\nКоманда EDIT NOTE позволяет вам перезаписать или обновить созданную вами заметку,"
                    "\nКоманда REMOVE NOTE удаляет раннее созданную заметку,"
                    "\nКоманда BREAK завершит редактирование заметок")
    while True:
        action = input('Введите команду: ')
        if action.lower() == 'new note':
            create_note()
        elif action.lower() == 'read note':
            read_note()
        elif action.lower() == 'edit note':
            edit_note()
        elif action.lower() == 'remove note':
            delete_note()
        elif action.lower() == 'break':
            break
        else:
            print('Не существующая команда')
            main()


display_notes()
