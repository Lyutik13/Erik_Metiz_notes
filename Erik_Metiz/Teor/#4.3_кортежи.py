# в картеже нельзя менять, добовлять, удалять
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Перебор всех значений в кортеже через for
for dimension in dimensions:
    print(dimension)

#Замена кортежа
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions  = (400, 100)         # заменили значение в переменной на новое
for dimension in dimensions:
    print(dimension)