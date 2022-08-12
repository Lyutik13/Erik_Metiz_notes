# country = {'code': 'RU', 'name': 'Russian', 'population': 144}   # 1-й способ
# # country = dict(code='RU', name='Russian')                      # 2-й способ
#
#  print(country['name'])
#
# print(country.items())
# for key, value in country.items():   # созданно 2-е переменные key и value. Через .items() выводим значение ключа(key)
#     print(key, ' - ', value)

                         # функции при работе со словарями:
country = {'code': 'RU', 'name': 'Russian', 'population': 144}

print(country['code'])        # или скобки ['']
print(country.get('name'))    # или .get('')

# country.clear()               # .clear очищение словаря
# country.pop('name')           # .pop удаляет выбраный элемент
# country.popitem()             # .popitem удаляет последний элемент

                         # вывод key or values or items
# print(country.keys())
# print(country.values())
# print(country.items())
                         # .update или замена
# country.update(code='EU')     # 1-й срособ через .update
# country['code'] = 'None'      # 2-й срособ через замену
# print(country)

person = {
    'user_1': {
        'first_name': 'Ehor',
        'last_name': 'Rostovsri',
        'age': 30,
        'address': ['г. Ростов', "ул. Какая-то", "д. 40"],
        'grades': {'math': 2, 'litorboll': 5}
    },
    'user_2': {
    }
          }
print(person['user_1']['grades']['math'])
print(person['user_1']['address'][1])
