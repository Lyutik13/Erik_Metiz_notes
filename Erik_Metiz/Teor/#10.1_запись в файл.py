# Чтобы записать текст в файл, необходимо вызвать open() со вторым аргументом,
# который сообщает Python, что вы собираетесь записывать данные в файл.
filename = 'files/programming.txt'

with open(filename, 'w') as file_object:  # 'w' запись в файл с нуля!
    file_object.write("I love and don't love Arma 3\n")

# Файлы можно открывать:
#   в режиме чтения                 ('r')
#   записи                          ('w')
#   присоединения                   ('a')
#   как чтение, так и запись в файл ('r+')

#  Многострочная запись добавляё в конец строки \n

# __________________________ Присоединение данных к файлу__________________________
with open(filename, 'a') as file_object:  # 'a' добавление к имеющемся
    file_object.write("I love all and vice versa\n")
    file_object.write("I love programming.\n")

with open(filename) as file_contents:
    print(file_contents.read().strip())
