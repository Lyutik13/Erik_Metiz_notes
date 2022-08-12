# ______________Изменение списка в функции ______________
def print_models(unprinted_designs, completed_models):
    # Имитирует печать моделей, пока список не станет пустым.
    # Каждая модель после печати перемещается в completed_models.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # Выводит информацию обо всех напечатанных моделях
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ______________ Запрет изменения списка в функции ______________
# Чтобы передать функции копию списка, можно поступить так:
# имя_функции(имя_списка[:])
uuunprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
cccompleted_models = []
print_models(uuunprinted_designs[:], cccompleted_models)
print(uuunprinted_designs)
print(cccompleted_models)


# ______________ Передача произвольного набора аргументов (*) *args______________
# Звездочка в имени параметра *toppings приказывает Python создать пустой
# кортеж с именем toppings и упаковать в него все полученные значения
def make_pizza(*toppings):
    """Выводит описание пиццы."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# ______________ Позиционные аргументы с произвольными наборами аргументов ______________
def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# ______________ Использование произвольного набора именованных аргументов (**kwargs)______________
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
