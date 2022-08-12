#################################### Перебор всех пар «ключ-значение»   .items() #######################################
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():          # .items() для просмотра всего
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#------------------primer-----------------------------
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
    print(f"{name.title()} 's favorite language is {language.title()}")

######################## Перебор всех ключей в словаре  .keys()  (CТАНДАРТНЫЙ for) #####################################
for name in favorite_languages.keys():
    print(name.title())
print('___________________________________________')

#------------------primer-----------------------------
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print('Hi', name.title())

    if name in friends:
        language = favorite_languages[name].title()
        # print('\t', name.title(), 'I see you love', language)
        print(f"\t {name.title()} I see you love {language.title()}!")

#Метод keys() также может использоваться для проверки того, участвовал ли конкретный человек в опросе:
if 'erin' not in favorite_languages:
    print("Erin, please take our poll!\n")

####################################### Перебор ключей словаря в определенном порядке . sorted() #######################
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):             # sorned() сортировка
    print(name.title(), "thank you for taking the poll.")

###################################### Перебор всех значений в словаре .values() #######################################
print("\tThe following languages have been mentioned:")
for language in set(favorite_languages.values()):         # set() убирает дубликаты
    print(language.title())
