# ____________________Изменение элементов в списке____________________

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'    # изменяем
print(motorcycles)

# ____________________Добавление элементов в список____________________

#Присоединение элементов в конец списка .append()
motorcycles.append('ducati')
print(motorcycles)

# Вставка элементов в список .insert()
motorcycles.insert(0, 'kavasaki')    # [0]- позиция в списке
print(motorcycles)

