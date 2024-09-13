#  Домашняя работа по уроку "Специальные методы классов"
#  Задача "Магические здания":

class House:
    def  __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floors) or int(new_floor) < 1 :
            print("Такого этажа не существует")
        else:
            for i in range(1, int(new_floor+1 )):
                print(i)

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return "Название: " + str(self.name) + ", кол-во этажей: " + str(self.number_of_floors)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))