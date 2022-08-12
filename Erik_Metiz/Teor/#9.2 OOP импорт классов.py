# _________________ импортируем классы из файла car: _________________

from car import Car

my_new_car = Car('BMW', 'X6', 2013)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 13
my_new_car.read_odometer()

from car import ElectricCar

my_new_tesla = ElectricCar('BMW', 'Z1', 2023)

print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()
my_new_tesla.fill_gas_tan()

# _________________ Импортирование нескольких классов из модуля: _________________
from car import Car, ElectricCar  # перечисляем!

car_1 = Car('Jeep', 'Chiroky', 2015)
print(car_1.get_descriptive_name())
kolhoz_elektrik = ElectricCar('zaz', 'turbo', 2022)
print(kolhoz_elektrik.get_descriptive_name())

# _________________ Импортирование всего модуля: _________________

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# _________________ Импортирование всех классов из модуля: _________________
# from имя_модуля import * (не рекомендуется! )

# _________________ Можно так же импортировать модуль в модуль _________________

# _________________ Использование псевдонимов _________________
# как в 8-й главе с функциями!

from car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
