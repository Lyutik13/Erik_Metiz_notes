# word = 'ViTya-vitya'
#
# print(len(word))         # .len() - считает все символы
# print(word.count('t'))   # .count("") - счётчик
# print(word.upper())      # .upper() - всё вверхний регистор
# print(word.isupper())    # .isupper() - FALSE если вся строка в нижнем регтстре
# print(word.islower())    # .islower() - True если если вся строка в верхнем регтстре
# print(word.lower())      # .lower() - весь текст в нижний регистр
# print(word.capitalize()) # .capitalize() - одна заклавная буква в верхнем
# print(word.find('i'))    # .find('') - поиск

# word2 = 'Vitya, Postov, Diman, Galya, Yamuar ....'
# name = word2.split(', ')
# print(word2.split(', '))   # .split(, ) - разбивает строку по введёному символу
# print(name[1])

# Primer автокоректор
word3 = 'Vitya, Postov, Diman, galya, yamuar ....'
name3 = word3.split(', ')        # разбиваем (.splitt('символ')

for el in range(len(name3)):     # range - диапозон от - до ( + метод len считаем символы)
    name3[el] = name3[el].capitalize()

print(name3)

result = ', '.join(name3)        # .join обьединение
print(result)