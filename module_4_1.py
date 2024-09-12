#  Домашняя работа по уроку "Модули и пакеты"
#  Задача "А как делить?":

from true_math import divide as div_0_inf
from fake_math import divide as div_0_err

result1 = div_0_err(69, 3)
result2 = div_0_err(3, 0)
result3 = div_0_inf(49, 7)
result4 = div_0_inf(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)