"""   Задание 1. Приложение заметки (Python)
Напишите проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её,
читать список заметок, редактировать заметку, удалять заметку.
"""
from datetime import datetime
from json import dumps
from io import StringIO
import csv

file_path = 'notes.csv'


def read_file(file_name):
    result = []
    with open(file_name, 'r', encoding='utf-8', newline='') as text_file:
        note_reader = csv.reader(text_file, delimiter=';')
        for note in note_reader:
            result.append(note)
    return result


def write_file(list_notes, file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as text_file:
        csv.writer(text_file, delimiter=';').writerows(list_notes)


def write_note_to_end_file(note, file_name):
    with open(file_name, 'a', encoding='utf-8', newline='') as text_file:
        csv.writer(text_file, delimiter=';').writerow(note)


def sort_key(lst):
    return int(lst[0])


def sort_by_id(list_notes):
    return sorted(list_notes, key=sort_key)


def filter_by_date(list_notes, date_filter):
    result = []
    for note in list_notes:
        if note[-1].split()[0] == date_filter:
            result.append(note)
    return result


def note_to_string(note, style='simple'):
    if style == 'simple':
        return '\n'.join(note[1:3])
    if style == 'txt':
        result = 'Идентификатор заметки = ' + note[0] + '\n'
        result += 'Заголовок заметки = ' + note[1] + '\n'
        result += 'Тело заметки = ' + note[2] + '\n'
        result += 'Дата заметки = ' + note[3]
        return result
    if style == 'json':
        columns = ['id', 'title', 'body', 'timestamp']
        return dumps(dict(zip(columns, note)), ensure_ascii=False)
    if style == 'csv':
        output = StringIO()
        csv.writer(output, delimiter=';', lineterminator='').writerow(note)
        return output.getvalue()
    return '\n'.join(note)


def print_note(note, style='simple'):
    print(note_to_string(note, style), '\n')


def print_list_notes(list_notes, style_list='simple'):
    for note in list_notes:
        print_note(note, style=style_list)


def next_id(list_notes):
    return int(list_notes[-1][0]) + 1


def date_time_now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def main():
    choice = ''
    while choice != '0':
        choice = input("""
        Выберите действие:
        1. Добавить заметку
        ---
        0. Выход
        """)
        if choice == '1':
            new_note = list()
            new_note.append(str(next_id(read_file(file_path))))
            new_note.append(input('Введите заголовок заметки: '))
            new_note.append(input('Введите тело заметки: '))
            new_note.append(date_time_now())
            write_note_to_end_file(new_note, file_path)
            print('Заметка успешно сохранена')


main()

