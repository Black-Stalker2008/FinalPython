import model as m
from os import path


def check_type_num(data: str) -> int:
    if data.isdigit():
        return int(data)
    return -1
    


def check_id_exist(id: int, id_list: list) -> int:
    count = 0
    for i in range(len(id_list)):
        if int(id_list[i]) == id:
            count += 1
    if count > 0:
        return id
    else:
        return -1