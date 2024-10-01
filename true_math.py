from math import inf        # импортируем бесконечность из библиотеки math

def divide(first, second):
    if second == 0:         # если second = 0 вывести бесконечность
        return inf
    else:                   # если же нет вывести результат деления
        return first / second


#В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second,
# но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

