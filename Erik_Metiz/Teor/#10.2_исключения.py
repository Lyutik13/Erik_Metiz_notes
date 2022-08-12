# Блоки try-except

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")


#  try-except-else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: \n")
    if first_number == 'q':
        break
    second_number = input("Second number: \n")
    if second_number == 'q':
        break
    try:                                                        # там где можит быть ошибка
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:                                   # обработка ошибки
        print("You can't divide by 0!")
    else:                                                       # продолжение зависимого кода
        print(answer)


# Обработка исключения FileNotFoundError (попытались открыть не существующий файл)
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:  # encoding. Он необходим в тех случаях, когда кодировка вашей системы
                                                 # по умолчанию не совпадает с кодировкой читаемого файла.
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# Анализ текста
filename = 'files/alice_10.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:                         # Подсчет приблизительного количества строк в файле.
    words = contents.split()  # метод split() для получения списка всех слов в книге
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


# Работа с несколькими файлами

