#Дополнительное практическое задание по модулю*
#  Дополнительное практическое задание по модулю: "Наследование классов."
#  Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
#   Задание "Они все так похожи":


class Figure:
    sides_count = 0

    def __init__(self,*,  __color, __sides):
       # self.filled = filled
        self.__sides = __sides
        self.__color = __color

        super().__init__()


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self,*new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side_length in new_sides:
            if side_length <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr_fig = 0
        for side in self.__sides:
            perimetr_fig += len(side)
        return perimetr_fig

    def set_sides(self, *new_sides):
        if not self.__is_valid_sides(*new_sides):
            return
        self.__sides = new_sides



class Circle(Figure):
    PI = 3.14159
    sides_count = 1

    def __init__(self,  __color, __sides): #, *args):
        #self.__sides = __sides
        #self.__color = __color
        super().__init__(self,__color, __sides)
        #self.__radius = int(args[3])/2/3.14159
        print(self.__color)
        print(self.__sides)
        #print(len(args))
    def get_square(self, __radius):
        return #3.14159 * self.__radius * self.__radius
        #__ 3,14159


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
print(circle1.get_sides())
circle1.set_color(55, 66, 77) # Изменится
circle1.set_sides(15) # Изменится
print(circle1.get_sides())