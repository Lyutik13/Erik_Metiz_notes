# Словарь в языке Python представляет собой совокупность пар «ключ-значение»

# __________________________Добавление новых пар «ключ-значение»__________________________
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# __________________________Изменение значений в словаре__________________________
alien_0['color'] = 'yellow'
print(alien_0)
print(f"naw color is: {alien_0['color']}")

# Рассмотрим более интересный пример: отслеживание позиции пришельца
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'color': 'green', 'points': 5}
print('Original position:', alien_0['x_position'])
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New position:', alien_0['x_position'])

#_________________________Удаление пар «ключ-значение»__________________________
del alien_0['points']
print(alien_0)

#_________________________get()__________________________(обработка ошибки)
#В первом аргументе метода get() передается ключ. Во втором необязательном аргументе можно передать значение,
# которое должно возвращаться при отсутствии ключа:
                      #1              #2
debag = alien_0.get('points', 'No point value assigned.')
print(debag)
