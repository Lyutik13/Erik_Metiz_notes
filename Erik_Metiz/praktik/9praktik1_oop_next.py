# 9.6
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Инициализирует атрибуты Restaurant."""
        print(f"\nThe restarant name is : {self.restaurant_name} and hi cuisine type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open !")

    def read_served(self):
        """выводит значение number_served"""
        print(f"Обслуженно : {self.number_served} посетителей")

    def set_number_served(self, guest):
        """Добовляем гостей заменой"""
        self.number_served = guest

    def increment_number_served(self, guests):
        """Добовляем гостей сложением"""
        self.number_served += guests


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ice', 'frukt', 'cheery', 'standart']

    def read_flavors(self):
        print(self.flavors)
        for flavor in self.flavors:
            print(f"viv Ice-ctram :{flavor.title()}")


my_IceCreamBox = IceCreamStand('Mumu', 'oll')
my_IceCreamBox.describe_restaurant()
my_IceCreamBox.read_flavors()


# 9.7 and 9.8
class User():
    def __init__(self, first_name, last_name, age, sity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sity = sity
        self.login_attempts = 0

    def describe_user(self):
        """Read info about user"""
        print(f"\n{self.first_name} {self.last_name} \nage: {self.age} \nSity: {self.sity}")

    def greet_user(self):
        """sey Hello"""
        print(f"Hello {self.first_name} {self.last_name} !!!")

    def increment_login_attempts(self):
        """Добавляем по 1 в login_attempts"""
        self.login_attempts += 1

    def read_login_attempts(self):
        print(f"Колличество входа в систему : {self.login_attempts}")

    def reset_login_attempts(self):
        if self.login_attempts >= 0:
            self.login_attempts = 0


class Privileges():  # для 9.8 создали новый класс для атребута Admen
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей", "Admin царь разрешенно всё!!!"]

    def show_privileges(self):
        print(f"Что можeт admen :")
        for privilege in self.privileges:
            print(f"{privilege.capitalize()}")


class Admin(User):
    def __init__(self, first_name, last_name, age, sity):
        super().__init__(first_name, last_name, age, sity)
        self.privileges = Privileges()
    #     self.privileges = ["разрешено добавлятьсообщения", "разрешено удалять пользователей",
    #                        "разрешено банить пользователей", "Admin царь разрешенно всё!!!"]
    #
    # def show_privileges(self):
    #     print(f"Что можeт {self.first_name} :")
    #     for privilege in self.privileges:
    #         print(f"{privilege}")


i_admin = Admin('Admin', 'Admin', 'Admin', 'Admin')
i_admin.describe_user()
# i_admin.show_privileges()
i_admin.privileges.show_privileges()


# 9.9
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

    def upgrade_battery(self):
        """апгрейт аккумулятора машины (battery_size) до 100"""
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar2(Car):
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя.Затем инициализирует атрибуты, специфические для электромобиля. """
        super().__init__(make, model, year)
        self.battery = Battery()  # используем Battery как атребут к ElectricCar2


my_sammer_car = ElectricCar2('jiguli', 2101, 1997)
print(my_sammer_car.get_descriptive_name())
my_sammer_car.battery.describe_battery()
my_sammer_car.battery.upgrade_battery()
my_sammer_car.battery.describe_battery()