#  Домашняя работа по уроку "Перегрузка операторов."
#  Задача "Нужно больше этажей":

class House:
    def  __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floors) or int(new_floor) < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, int(new_floor+1 )):
                print(i)

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return "Название: " + str(self.name) + ", кол-во этажей: " + str(self.number_of_floors)

    def __eq__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors == other.number_of_floors:
                answ_ = True
        return answ_

    def __Lt__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors < other.number_of_floors:
                answ_ = True
        return answ_

    def __Le__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors <= other.number_of_floors:
                answ_ = True
        return answ_

    def __gt__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors > other.number_of_floors:
                answ_ = True
        return answ_

    def __ge__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors == other.number_of_floors:
                answ_ = True
        return answ_

    def __ne__(self, other):
        answ_ = False
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            if self.number_of_floors != other.number_of_floors:
                answ_ = True
        return answ_

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        return  House.__add__(self, value)

    def __iadd__(self, value):
        return  House.__add__(self, value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__