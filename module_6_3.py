#  Домашнее задание по теме "Множественное наследование
#  Цель: закрепить знания множественного наследования в Python.
#
# Задача "Мифическое наследование":

class Horse():
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx
