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


def write_note_to_end_file(note, file_name):
    with open(file_name, 'a', encoding='utf-8') as text_file:
        print(';'.join(note), file=text_file)


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


def print_note(note, style='simple'):
    if style == 'simple':
        print('', note[1], note[2], sep='\n')
    elif style == 'txt':
        print('\nИдентификатор заметки =', note[0])
        print('Заголовок заметки =', note[1])
        print('Тело заметки =', note[2])
        print('Дата заметки =', note[3])
    elif style == 'json':
        print(f'{{\"id\":{note[0]},\"title\":\"{note[1]}\",\"body\":\"{note[2]}\",\"date\":\"{note[3]}\"}}')
    elif style == 'csv':
        print(';'.join(note))
    else:
        print('\n'.join(note))


def print_list_notes(list_notes, style_list='simple'):
    for note in list_notes:
        print_note(note, style=style_list)


