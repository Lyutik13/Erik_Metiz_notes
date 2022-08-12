# 9.13 kubik
from random import randint


class Die():
    def __init__(self, sides=6):
        """Инициализирует атрибуты кубика."""
        self.sides = sides
        self.list = []

    def roll_die(self):
        """Бросок кубика - 1"""
        print(randint(1, 6))

    def more_roll_die(self, quantity):
        """задаем колличество бросков кубика и сохраняем """
        for roll in range(quantity):
            # my_kubik.roll_die()   # без добавления в список
            self.list.append(randint(1, 6))

    def read_roll_list(self):
        """читаем list список"""
        print(self.list)


my_kubik = Die()
my_kubik.more_roll_die(10)
my_kubik.read_roll_list()

# 9.14 loterea
from random import choice

lochtron_2022 = [1, 5, 6, 'Z', 'O', 'V', 2, 0, 8, 'U', 9, 'R', 3, 4, 7]
rezult = []


# вручную
# put_out = choice(lochtron_2022), choice(lochtron_2022), choice(lochtron_2022), choice(lochtron_2022)
# print(put_out)

# функцией
def putin_out(quantity):
    """задаём количество считываний из списка и добавляем в новый"""
    for x in range(quantity):
        rezult.append(choice(lochtron_2022))


putin_out(4)
print(rezult)

# 9.15 взято всё из 9.14
my_tiket = ['Z', 'O', 'V', 1]
test_fortune = True
counter = 0

while test_fortune:
    if rezult != my_tiket:
        print(rezult)
        rezult.clear()
        counter += 1
        putin_out(4)

    elif rezult == my_tiket:
        print(f"You WIN!!! Сombination is{my_tiket} and own attempt {counter}")
        break
