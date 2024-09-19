#  Домашнее задание по теме "Множественное наследование
#  Цель: закрепить знания множественного наследования в Python.
#
# Задача "Мифическое наследование":


class Horse:
    x_distance = 0
    sound_hors = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
         self.sound = super().sound_hors
         self.sound = super().sound

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
#        print(self.sound_hors)             # помним голос первого родителя тоже!
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
