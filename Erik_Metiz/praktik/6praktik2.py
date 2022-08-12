# 6.7
print("____________________________# 6.7____________________________")
humans1 = {'first_name': 'viktor',
           'last_name': 'lyutikov',
           'age': '24',
           'city': 'podolck'}

humans2 = {'first_name': 'diman',
           'last_name': 'lebedev',
           'age': '27',
           'city': 'moscow'}

humans3 = {'first_name': 'egor',
           'last_name': 'shehterman',
           'age': 'many',
           'city': 'rostov'}

peoples = [humans1, humans2, humans3]

for people in peoples:
    print("\n")
    for key, vailue in people.items():
        print(f" {key.title()} : {vailue.title()}")

# 6.10
print("____________________________# 6.10____________________________")
oll_favjrite_ints = {
    'Viktor': ['13', '0', '5', '7'],
    'Diman': ['1992'],
    'sergo': ['0'],
    'Niki': ['18'],
    'margelov': ['0']
}
count = 1

for name, values in oll_favjrite_ints.items():
    if len(values) > count:
        print(f"\n{name.title()}'s favorite int are:")
        for value in values:
            print(f"\t{value}")
    else:
        for value in values:
            print(f"{name.title()} s favorite int is \n {value}")

# добавил в список
oll_favjrite_ints['Viktor'].append('555')
print(oll_favjrite_ints['Viktor'])

# 6.8
print("____________________________# 6.8____________________________")
laima = {'viv': 'dog',
         'name_owner': 'viktor'
         }
kesha = {'viv': 'bert',
         'name_owner': 'niki'
         }
pets = [laima, kesha]

for pet in pets:
    for vivs, name_owners in pet.items():
        print(vivs, name_owners)

# 6.9
print("____________________________# 6.9____________________________")


# none