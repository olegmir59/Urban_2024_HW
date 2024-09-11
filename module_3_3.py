
#  Самостоятельная работа по уроку "Распаковка позиционных параметров".
#  Домашнее задание по уроку "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print("1.Функция с параметрами по умолчанию:")
print_params()
print_params('строка789')
print_params(65,'строка789')
print_params('строка789',6, [23, 8,9])
print()
print_params(b = 25)
print_params(c = [1,2,3])
print()

print("2.Распаковка параметров:")
values_list = [21, 'строка789', False]
values_dict = {'a':9, 'b':'строка789', 'c':True}

print_params(*values_list)
print()
print_params(*values_dict)
print_params(**values_dict)
print()
print("3.Распаковка + отдельные параметры:")
values_list_2 = [99, 'Строка123' ]
print_params(*values_list_2, 79)
