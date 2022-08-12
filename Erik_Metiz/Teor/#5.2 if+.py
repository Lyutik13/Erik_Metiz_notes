# Проверка специальных значений
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print('Adding:', requested_topping)
print("\nFinished making your pizza!")
print('_______________')

# Проверка специальных значений
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print('sorry dont have mushrooms')
    else:
        print('Adding', requested_topping)

# Проверка наличия элементов в списке
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding in pizza:', requested_toppings)
    print("\nFinished making your pizza!")
else:
    print('Are you sure you want a plain pizza?\n__________________Множественные списки_________________')

# Множественные списки
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Addind:', requested_topping)
    else:
        print('we dont have:', requested_topping)
