import os
from os import path


def what_the_way(the_way, file_name):
    new_way = os.path.join(the_way, file_name)
    return new_way

file = 'Лаба1.docx'
way = 'C:\\Users\\Никита\\Desktop\\Projects\\Отчеты по Питону'
file_way = what_the_way(way, file)
print(file_way)
