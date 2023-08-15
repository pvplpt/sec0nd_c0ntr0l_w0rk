"""   Задание 1. Приложение заметки (Python)
Напишите проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её,
читать список заметок, редактировать заметку, удалять заметку.
"""

file_path = 'notes.csv'


def read_file(file_name):
    result = []
    with open(file_name, 'r', encoding='utf-8') as text_file:
        for line in text_file:
            result.append(line.strip().split(';'))
    return result


def write_file(list_notes, file_name):
    with open(file_name, 'w', encoding='utf-8') as text_file:
        for note in list_notes:
            print(';'.join(note), file=text_file)


