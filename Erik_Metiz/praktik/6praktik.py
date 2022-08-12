# 6.1
humans = {'first_name': 'viktor',
          'last_name': 'lyutikov',
          'age': '24',
          'city': 'podolck'}

for key, vailue in humans.items():
    print(f"{key} : {vailue}")

# 6.2
oll_favjrite_ints = {'Viktor': 13,
                     'Diman': 1992,
                     'sergo': 0,
                     'Niki': 18,
                     'Margelov': 0
                     }

print(oll_favjrite_ints['Viktor'])

for name, value in oll_favjrite_ints.items():
    print(name, 'favorite int is', value)

# 6.3
glossorys = {'команда': 'if', 'списки': 'числовые и буквенные', 'команды': 'if elif elce', 'переменные': 'значения',
            'комментарии': '#'}
zdsfg= {}

for opr, znach in glossorys.items():
    print(opr.title(), 'is :', znach.lower())
