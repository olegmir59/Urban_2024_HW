#  Домашнее задание по теме "Множественное наследование
#  Цель: закрепить знания множественного наследования в Python.
#
# Задача "Мифическое наследование":

class Horse():
    def __init__(self, x_distance, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        Horse.x_distance = dx


class Eagle():
    def __init__(self, y_distance, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance = self.y_distance + dy

class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0, sound="UUUUU"):
        Horse().__init__(x_distance)
        Eagle().__init__(y_distance,sound)
    #    Eagle().__init__(sound)


    def move(self, dx, dy):
        super().run(dx)
        Eagle().fly(dy)

    def get_pos(self):
        return (Horse().x_distance, Eagle().y_distance)

    def voice(self):
        print(Eagle().sound)


p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
#p1.move(-5, 20)
#print(p1.get_pos())

#p1.voice()
