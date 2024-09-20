#Дополнительное практическое задание по модулю*
#  Дополнительное практическое задание по модулю: "Наследование классов."
#  Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
#   Задание "Они все так похожи":


class Figure:
    sides_count = 0
    def __init__(self, *, filled, __sides, __color):
        self.filled = filled
        self.__sides = __sides
        self.__color = __color

        super().__init__()


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r in range(0, 256) and g in range(0, 256) and b in range(0, 256)

    def set_color(self, r, g, b):
        if self.__is_valid_color( r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self,*args):
        if len(args) == self.sides_count:
            for side_length  in args:
                if side_length <= 0:
                    return False
            else:
                return True
        else:
            return False

