#  Дополнительное практическое задание по модулю*
#  Дополнительное практическое задание по модулю: "Подробнее о функциях."

def calculate_structure_sum(data_structure):
    sum_nums_lens = 0
    for obj_1 in data_structure:
        if isinstance(obj_1, int):
            sum_nums_lens += obj_1                  # добавить целое число
        if isinstance(obj_1, float):
            sum_nums_lens += obj_1                  # добавить дробное число
        if isinstance(obj_1, str):
            sum_nums_lens += len(obj_1)             # добавить длину строки
        if isinstance(obj_1, tuple):
            sum_nums_lens += calculate_structure_sum(obj_1)    # рекурсивный вызов функции, для каждой внутренней структуры
        if isinstance(obj_1, set):
            sum_nums_lens += calculate_structure_sum(obj_1)
        if isinstance(obj_1, list):
            sum_nums_lens += calculate_structure_sum(obj_1)
        if isinstance(obj_1, dict):
            sum_nums_lens += calculate_structure_sum(obj_1.items())
    return sum_nums_lens

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
