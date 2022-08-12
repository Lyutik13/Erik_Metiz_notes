#Удаление элемента с использованием команды del (Если вам известна позиция элемента)

motorcycles = ['honda', 'yamaha', 'suzuki', 'Harley-Davidson', 'kawasaki', 'bmw', 'Harley-Davidson', 'иж', 'Днепр']
del motorcycles[1]
print(motorcycles)

# Удаление элемента с использованием метода pop() последний!  (значение, удаляемое из списка, будет как-то использоваться)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Извлечение элементов из произвольной позиции списка .pop(1)

popped_motorcycle = motorcycles.pop(1)    # просто укажем позицию эл. в списке
print(motorcycles)
print(popped_motorcycle)

# Удаление элементов по значению / когда неизвестна позиция .remove()  (удаляет только один эл. из списка)

my_drem = 'Harley-Davidson'
motorcycles.remove(my_drem)   # можно удалить через переменную для её использования
print(motorcycles)
print('Моя мечта это -', my_drem)