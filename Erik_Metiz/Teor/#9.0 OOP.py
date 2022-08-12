# ______________________ Создание и использование класса ______________________
# (смотри пример 9praktik_oop)

# ______________________ Работа с классами и экземплярами ______________________
# Назначение атрибуту значения по умолчанию
class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # ( Назначение атрибуту значения по умолчанию)

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


#                              Изменение значений атрибутов ( 3 способа )

# Значение атрибута можно изменить одним из трех способов: изменить его прямо
# в экземпляре, задать значение при помощи метода или изменить его с приращением
# (то есть прибавлением определенной величины) при помощи метода.

# 1-й Прямое изменение значения атрибута
# (Чтобы изменить значение атрибута, проще всего обратиться к нему прямо через экземпляр.)
class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  # ( прямое обращение к атрибуту )
my_new_car.read_odometer()


# ______________________________________________________________________________________________________________________

# 2-й Изменение значения атрибута с использованием метода
# (Вместо того чтобы изменять атрибут напрямую, вы передаете новое значение методу,
# который берет обновление атрибута на себя.)

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):  # (добавили новый метод, для обновления атребута odometer_reading и проверку!)
        """Устанавливает на одометре заданное значение.При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            """Устанавливает заданное значение на одометре."""
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(66)
my_new_car.read_odometer()


# ______________________________________________________________________________________________________________________

# 3-й Изменение значения атрибута с приращением

class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            """Устанавливает заданное значение на одометре."""
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Проверка на обратную прокрутку и прибавление пробега к имеющемся"""
        if miles <= -1:
            print("You can't roll back an odometer again!")
        else:
            """Увеличивает показания одометра с заданным приращением."""
            self.odometer_reading += miles   # ( приращение к имеющемся значению)


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
