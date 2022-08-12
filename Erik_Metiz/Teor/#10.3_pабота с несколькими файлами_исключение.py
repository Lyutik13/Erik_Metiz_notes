# Работа с несколькими файлами
def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # pass oшибки без уведомления пользователя
        print(f"Sorry, the file {filename} does not exist.")
    else:  # Подсчет приблизительного количества строк в файле.
        words = contents.split()  # метод split() для получения списка всех слов в книге
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'files/alice_10.txt'
count_words(filename)
print('______________________________')

filenames = ['files/alice_10.txt', 'siddhartha.txt', 'files/moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# Ошибки без уведомления пользователя pass

