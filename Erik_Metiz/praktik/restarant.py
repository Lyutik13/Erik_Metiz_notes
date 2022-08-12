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
