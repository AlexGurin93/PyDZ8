# 2)Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки
import random


class School:
    def __init__(self, name, group, progress):
        self.name = name
        self.group = group
        self.progress = progress

    def show_name(self):
        name = {'Иванов', 'Петров', 'Сидоров'}
        return name

    def show_group(self):
        group = {'9', '10', '11'}
        return group

    def show_progress(self):
        progress = random in range(2, 5)
        return progress

    def show_info(info):
        print(f'Имя={info.name()}, успеваемость = {info.progress()}')
# Код отрабатывается, но ничего не происходит, надеюсь вы укажете на ошибку,спасибо