#Дополнительное практическое задание по модулю*
#  Дополнительное практическое задание по модулю: "Наследование классов."
#  Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
#   Задание "Они все так похожи":


class Figure:
    sides_count = 0

    def __init__(self,  color, sides):
        self.__color = color
        self.__sides = sides
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
        match self.sides_count:
            case 0:                 # Figure
                return 0
            case 1:                 # Circle , отрезок
                return self.__sides
            case _:                 # Triangle (3,4,5),   четырехугольник (3,4,5,6)  и  бесконечныое множество фигур
                perimetr_fig = 0
                for side in self.get_sides():
                    perimetr_fig += side
                return perimetr_fig

    def set_sides(self, new_sides):
        if not self.__is_valid_sides(new_sides):
            return
        self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides,filled=False):
        super().__init__(color, sides)
        self.filled = filled
        self.__radius = float(self.get_sides()/2/3.14159)

    def get_square(self):
         return 3.14159 * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides,filled=False):
        super().__init__(color, sides)
        self.filled = filled

    def get_square(self):
        abc_list = self.get_sides()
               # стороны треугольника
        a = abc_list[0]
        b = abc_list[1]
        c = abc_list[2]
                # Полупериметр треугольника
        s = (a + b + c) / 2
                # Формула Герона для площади треугольника
        return __import__('math').sqrt(s * (s - a) * (s - b) * (s - c))

circle1 = Circle((200, 200, 100), (10))  # (Цвет, стороны)
triangle1 = Triangle((100, 199, 199),(3,5,4))

print(circle1.get_sides())
circle1.set_color(55, 66, 77) # Изменится
circle1.set_sides(15)                  # Изменится
print(circle1.get_sides())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
#cube1 = Cube((222, 35, 130), 6)

print(" Проверка на изменение цветов:")
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
#cube1.set_color(300, 70, 15) # Не изменится
#print(cube1.get_color())

print(" Проверка на изменение сторон")
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
#print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(" Проверка периметра (круга), это и есть длина:")
print(len(circle1))
print(len(triangle1))

print(" Проверка площади(круга)")
print(circle1.get_square())
print(triangle1.get_square())
# Проверка объёма (куба):
#print(cube1.get_volume())
