#  Домашнее задание по теме "Зачем нужно наследование"
#  Цель: применить базовые знания о наследовании классов для решения задачи
#
# Задача "Съедобное, несъедобное":

class Animal():
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name

    def eat(self, food):
        if food.edible:
            print(self.name, " съел ", food.name)
            self.fed = True
        else:
            print(self.name, " не стал есть ")
            self.alive = False


class Mammal(Animal):
    def __init__(self,  name):
        Animal.__init__(self, name)

class Predator(Animal):
    def __init__(self,  name):
        Animal.__init__(self, name)


class Plant():
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Flower(Plant):
    def __init__(self, name,edible=False):
        Plant.__init__(self, name, edible=False)

class Fruit(Plant):
    def __init__(self, name, edible=False):
        Plant.__init__(self, name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(a2.name)
print(p1.name)
print(p2.name)
print()
print(p1.edible)
print(p2.edible)
print(" до еды ")
print(a1.name, "жив ? : ", a1.alive)
print(a2.name, " накормлен ? : ", a2.fed)

a1.eat(p1)
a2.eat(p2)
print(" после еды")
print(a1.name, "жив ? : ",a1.alive)
print(a2.name, "накормлен ? : ",a2.fed)
