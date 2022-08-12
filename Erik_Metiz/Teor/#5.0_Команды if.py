cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Проверка вхождения значений в список  in

if 'bmw' in cars:
    print('yes')

# Проверка отсутствия значения в списке  not in
my_car = 'BMW'
if my_car not in cars:
    print('not')
