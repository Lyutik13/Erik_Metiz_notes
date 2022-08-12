# _______________ импортируем функцию из pizza.py _______________
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# _______________ Импортирование конкретных функций _______________
# from имя_модуля import функция_0, функция_1, функция_2
#            (пример)
from pizza import make_pizza

make_pizza(20, 'pepperoni')

# _______________ Назначение псевдонима для функции _______________
# from имя_модуля import имя_функции as псевдоним
#              (пример)
from pizza import make_pizza as mp

mp(8, 'cheese')
# _______________ Назначение псевдонима для модуля _______________
# import имя_модуля as псевдоним
import pizza as p

p.make_pizza(30, 'pepperoni')

# _______________ Импортирование всех функций модуля _______________ (нежелательно!!!)
# from имя_модуля import *

from pizza import *

make_pizza(1, 'fo TJD', )

tutu()
