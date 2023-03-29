from os import path
import csv
from prettytable import PrettyTable
import sys
import datetime

def last_id():
    with open('last_id.txt', 'r', encoding='utf-8') as l_f:
        last_id = l_f.read()
        return last_id

def write_file(file, data):
    with open(file, 'a', encoding='utf-8') as t_file:
        file_writer = csv.writer(t_file, delimiter="~", lineterminator="\n")
        file_writer.writerow(data)

def write_file_w(file, data):
    with open(file, 'w', encoding='utf-8') as t_file:
        file_writer = csv.writer(t_file, delimiter="~", lineterminator="\r")
        file_writer.writerow(data)

def read_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as t_file:
            csv.reader(t_file, delimiter='~')
            all_notes = []
            for row in t_file:
                str_note = "".join(row)
                list_note = str_note.strip().split('~')
                all_notes.append(list_note)
        return all_notes
    else:
        print("Файл не найден в системе!")

def get_table(file):
    list_all_notes = read_file(file)
    t = PrettyTable(list_all_notes[0])
    for i in range(1, len(list_all_notes)):
        t.add_row(list_all_notes[i])
    print(t)

def find_info(file, data: str) -> list:
    find_list = []
    id_find_list = []
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        for j in range(len(list_all_notes[i])):
            if str(list_all_notes[i][j]).find(data) == -1:
                pass
            else:
                find_list.append(list_all_notes[i])
                id_find_list.append(list_all_notes[i][0])
                break
    for k in range(len(find_list)+1):
        if k == 0:
            write_file_w('Find_info.csv', list_all_notes[k])
        else:
            write_file('Find_info.csv', find_list[k-1])
    get_table('Find_info.csv')
    return id_find_list

def add_text(file):
    id = last_id()
    id = int(id) + 1
    id_w = str(id)
    with open('last_id.txt', 'w', encoding='utf-8') as l_f:
        l_f.write(id_w)
    date = get_date()
    note = input('Введите заметку: ').lower()
    status = input('Введите статус: ').lower()
    new_note = [id, date, note, status]
    write_file(file, new_note)
    print('Заметка успешно добавлена!')
    print('Обновлённый список заметок')
    get_table(file)

def change_info(file, id: int, op: int):
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        if list_all_notes[i][0] == str(id):
            list_all_notes[i][1] = get_date()
            if op == 1:
                list_all_notes[i][2] = input('Перепешите заметку: ').lower()
            elif op == 2:
                list_all_notes[i][3] = input('Измените статус заметки: ').lower()
            elif op == 3:
                list_all_notes[i][2] = input('Перепешите заметку: ').lower()
                list_all_notes[i][3] = input('Измените статус заметки: ').lower()

    for j in range(len(list_all_notes)):
        if j == 0:
            write_file_w(file, list_all_notes[j])
        else:
            write_file(file, list_all_notes[j])
    print('Данные успешно изменены!')
    print('Обновлённый список заметок')
    get_table(file)

def delete_info(file, id: int):
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        if list_all_notes[i][0] == str(id):
            list_all_notes.pop(i)
            break
    for j in range(len(list_all_notes)):
        if j == 0:
            write_file_w(file, list_all_notes[j])
        else:
            write_file(file, list_all_notes[j])
    print('Заметка успешно удалена!')
    print('Обновлённый список заметок')
    get_table(file)
    id = last_id()
    id = int(id) - 1
    id_w = str(id)
    with open('last_id.txt', 'w', encoding='utf-8') as l_f:
        l_f.write(id_w)

def get_date():
    now = datetime.datetime.now()
    day = str(now.day)
    year = str(now.year)
    monthint = now.month
    if monthint < 10:
        date = day + "-" + "0" + str(now.month) + "-" + year
    else:
        date = day + "-" + str(now.month) + "-" + year
    return date