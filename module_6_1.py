#  Домашнее задание по теме "Зачем нужно наследование"
#  Цель: применить базовые знания о наследовании классов для решения задачи
#
# Задача "Съедобное, несъедобное":

class Animal:
    def __init__(self, alive=True, fed=False, name=''):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        pass

class Mammal(Animal):
    def __init__(self, food, name=''):
        self.food = food
        self.name = name

class Predator(Animal):
    def __init__(self, food, name=''):
        self.food = food
        self.name = name

class Plant:
    def __init__(self, edible=False, fed=False, name=""):
        self.edible = edible
        self.fed = fed
        self.name = name

class Flower(Plant):
    def __init__(self, food, name=''):
        self.food = food
        self.name = name

class Fruit(Plant):
    def __init__(self, food, name=''):
        self.food = food
        self.name = name

