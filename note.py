from os import path

def build_note(note_text, note_name):
    with open(f"{note_name}.txt", mode = 'w', encoding= 'utf-8') as file:
        file.write(note_text)
    print(f"Заметка {note_name} создана.")


def create_name():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    build_note(note_text, note_name)


def read_note():
    note_name = input("Введите название заметки: ")
    if (path.isfile(f'{note_name}.txt')):
        with open(f"{note_name}.txt", mode='r', encoding='utf-8') as file:
            print(file.read())
    else:
        print("Заметка не найдена")

read_note()