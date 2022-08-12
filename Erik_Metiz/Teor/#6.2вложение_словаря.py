#                                             Список словарей

################################################ Вложения словарей в список ############################################
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print("---------------------------------------------")

aliens = []
for aliens_number in range(30):
    new_aliens = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[0:1]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
print("_____________________________________________________________________")

########################################### Список в словаре ###########################################################
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust'].upper()}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping.title())
print("__________________________________________________________")

# ______________________primer---------------------------
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
count = 1
for name, languages in favorite_languages.items():
    if len(languages) > count:  # условие по счётчику
        print(f"{name.title()} 's favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        for language in languages:
            print(f"{name.title()} h’s favorite language is: {language.title()}")
print("__________________________________________________")

################################### Словарь в словаре ##################################################################
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername:", username)
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()
    print("\tFull name:", full_name)
    print("\tLocation:", location)