#  Домашняя работа по уроку "Различие атрибутов класса и экземпляра."
#  Задача "История строительства":

class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


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
    def __del__(self):
        print(self.name,'снесён, но он останется в истории')


h0 = House('Небоскёб Призрак', 110)
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print()
print("Список созданных домов: ",  House.houses_history)
print()
print("Перед завершением программы удаляются все оставшиеся объекты, поэтому")
print("Список удаленных оставшихся созданных домов: ")
