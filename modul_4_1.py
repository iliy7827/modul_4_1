import fake_math as fak # импортируем данные из модуля fake_math и придаем ему имя fake
import true_math as tru # импортируем данные из модуля true_math и придаем ему имя true


fake_divide = fak.divide # вызываем функцию fak
true_divide = tru.divide # вызываем функцию tru
                     
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
                        # вызываем результаты работы функций
print(result1)
print(result2)
print(result3)
print(result4)


