"""Классы для представления машин с бензиновым и электродвигателем."""


# ----------------------------------------------------------------------------------------------------------------------
class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tan = 70

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"\n{self.make} {self.model}, year: {self.year}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tan(self):
        """info about gas tank this car"""
        print(f"This car have gas tank : {self.gas_tan} l.")


# ----------------------------------------------------------------------------------------------------------------------
class Battery():
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=80):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        range_car = 0
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 80:
            range_car = 260
        elif self.battery_size == 100:
            range_car = 315
        print(f"This car can go about {range_car} miles on a full charge.")


# ----------------------------------------------------------------------------------------------------------------------
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.Затем инициализирует атрибуты, специфические для электромобиля. """
        super().__init__(make, model, year)
        self.battery = Battery()  # используем Battery как атребут к ElectricCar2

    # Переопределение методов класса-родителя (изменение метода родителя в потомке)
    def fill_gas_tan(self):  # пишем тот же метод и изменяем его как нам надо!
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!\n")
