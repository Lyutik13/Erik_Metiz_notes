try:
    with('texe.txt', 'r', encodings)
except FileNotFoundError:
    print('файл не найден')
finally:

