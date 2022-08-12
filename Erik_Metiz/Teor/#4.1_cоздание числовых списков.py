# Функция range()
for value in range(6):     # or (1, 6)  диапозон
    print(value)

# Использование range() для создания числового списка
numbers = list(range(1, 6))
print(numbers)

# Функция range() также может генерировать числовые последовательности, пропуская числа в заданном диапазоне.
even_numbers = list(range(2,11,2))
print(even_numbers)

# С помощью функции range() можно создать практически любой диапазон чисел.
# Например, как бы вы создали список квадратов всех целых чисел от 1 до 10?

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# Простая статистика с числовыми списками   (подсчёт min max sum в спмске)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)
print("min:", min(digits), "max:", max(digits), "sum:", sum(digits))

#Генераторы списков             (тоже создание списка, но быстрее)
squares_1 = [value_1**2 for value_1 in range(1, 11)]
print(squares_1)