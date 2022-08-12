# 6.4
glossorys = {'команда': 'if', 'списки': 'числовые и буквенные', 'команды': 'if elif elce', 'переменные': 'значения',
            'комментарии': '#'}
glossorys['словари'] = '{key: vaily}'

for name, vaily in glossorys.items():
    print(f"{name} is: {vaily} !")
# 6.5
rivers = {'nile': 'egypt', 'volga': 'russia', 'don': 'ukraina', }
for river, cauntry in rivers.items():
    print(f"The {river.title()} runs through {cauntry.upper()}")

for rriver in rivers.keys():
    print(rriver)

for cauntrys in rivers.values():
    print(cauntrys)

# 6.6  oprosnik
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

opros = ['jen', 'vitya', 'olya', 'phil', ]

for name in opros:
    if name in favorite_languages.keys():
        print(name.title(), 'Проходить опрос не надо!')
    else:
        print(name.title(), 'Прохйти опрос !')
    # if name not in favorite_languages.keys():
    #     print(name.title(), 'Прохйти опрос !')