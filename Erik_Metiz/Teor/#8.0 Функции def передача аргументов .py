# Определение функции
def sey_hello():
    """вывод приветствия"""
    print("hello")


sey_hello()


# Передача информации функции
def sey_hello(username):
    """вывод приветствия"""
    print(f"hello {username.title()}")


sey_hello('viktor')


# ---------------------------- Передача аргументов ----------------------------

# Позиционные аргументы
def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')


# Именованные аргументы
def describe_pet(animal_type, pet_name):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')


# Значения по умолчанию
def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')
