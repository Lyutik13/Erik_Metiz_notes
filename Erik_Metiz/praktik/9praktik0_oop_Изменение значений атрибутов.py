# 9.1
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restarant name is : {self.restaurant_name} and hi cuisine type is : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open !")


my_restaurant = Restaurant('Shaurma', 'vostok')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9.2
your_restaurant = Restaurant('Russian tea', 'more')
your_restaurant.describe_restaurant()

him_restaurant = Restaurant('Pizza_24', 'Italy')
him_restaurant.describe_restaurant()

burger_namber_1 = Restaurant('Burger_namber_1', 'Europe')
burger_namber_1.describe_restaurant()


# 9.3
class User():
    def __init__(self, first_name, last_name, age, sity):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sity = sity

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} \nage: {self.age} \nSity: {self.sity}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} !!!")


i = User('Viktor', 'Lyutikov', '24', 'Podolsk')
i.describe_user()
i.greet_user()

gad = User('Diman', 'Sergeevich', '27', 'Moscow')
gad.describe_user()
gad.greet_user()

galya = User('Galya', 'Chmo', '20', 'Adler')
galya.describe_user()
galya.greet_user()


# 9.4
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
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


my_restaurant = Restaurant('Shaurma', 'vostok')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.read_served()
my_restaurant.set_number_served(15)
my_restaurant.read_served()
my_restaurant.increment_number_served(20)
my_restaurant.read_served()


# 9.5
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


i = User('Viktor', 'Lyutikov', '24', 'Podolsk')
i.describe_user()
i.greet_user()
i.increment_login_attempts()
i.read_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.read_login_attempts()
i.reset_login_attempts()
i.read_login_attempts()
