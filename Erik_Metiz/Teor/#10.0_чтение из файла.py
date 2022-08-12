# _________________________ Чтение из файла всё _________________________
# Чтение всего файла
"""программа открывает этот файл из папки files, читает его и выводит содержимое на
экран :"""
with open('files/pi_digits.txt') as file_object:  # with закрывает файл после того, как надобность в нем отпадет cам!
    contents = file_object.read()
    print(contents.rstrip())  # удаляет все пропуски в конце строки
    # print(contents) со строкой в конце!

# test primer! из других папок!
test_file = 'V:/PycharmProjects/lern/Erik_Metiz/praktik/test_files/test1'
# или так
x = 'V:\\PycharmProjects\\lern\\Erik_Metiz\\praktik\\test_files\\test1'
with open(test_file) as test:
    contents1 = test.read()
    print(contents1)

# _________________________ Чтение по строкам _________________________
with open('files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# _________________________ Создание списка строк по содержимому файла _________________________
file_name = 'files/pi_digits.txt'
with open(file_name) as file_object1:
    lines = file_object1.readlines()  # метод readlines() последовательно читает каждую строку из файла
    # и сохраняет ее в списке. Список сохраняется в переменной lines
for line in lines:
    print(line.rstrip())

# _________________________ Работа с содержимым файла удаение пропусков strip()_________________________
filename = 'files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # Чтобы удалить пропуски, достаточно использовать strip() вместо rstrip()

print(pi_string)
print(len(pi_string))  # len() подсчёт символов

# _________________________ Большие файлы: 1 миллион цифр_________________________
filename1m = 'V:\\PycharmProjects\\lern\\Erik_Metiz\\praktik\\test_files\\pi_million_digits.txt'
with open(filename1m) as file_object1m:
    lines1m = file_object1m.readlines()
pi_string1m = ''
for line1m in lines1m:
    pi_string1m += line1m.strip()

print(f"{pi_string1m[:52]}...")
print(len(pi_string1m))

# _________________________ Проверка дня рождения (списка)_________________________
# берём пример из "Большие файлы: 1 миллион цифр" дописываем
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string1m:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
