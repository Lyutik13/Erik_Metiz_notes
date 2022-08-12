             # запись в файл через 'w' or 'a'
                         # w

# file = open('data/text.txt', 'w')  # w для написания,
#
# file.write('Hello')                # .write команда для написания   \n перенос строки
# file.write('!!!')
#
# file.close()                       # не забывай закрывать!

                          # a

# file = open('data/text.txt', 'w')  # a для добавления,
#
# file.write('Hello')
# file.write('!!!\n')
#
# file.close()

                        #primtr
# data = input('Ведите текст :\n')
#
# file = open('data/text.txt', 'a')    # 'w' or 'a' выбирай
#
# file.write(data + '\n')
#
# file.close()

file = open('data/text.txt', 'r')         # 'r' чтение файла

# print(file.read())                        # можно указать число в .read(5) для чтения нескольких символов

for line in file:                           # или можно создать цикл для вывода построчно
    print(line)                             # если не хочу пропусков строки добавлю (line, end='')

file.close()