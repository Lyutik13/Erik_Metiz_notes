only_int = 0
while only_int == 0:                                 # задали переменную если > 0 то while заканчивается
    try:                                             # Обработчик исключений try:
        only_int = int(input('Ведите число:\n'))
        only_int += 5
        print(only_int)
    except ValueError:                               # except + имя ошибки (можно много отследить)
        print('Только числа')
    else:                                            # else выполняется если после try, если не выполнился except
        print('else')
    finally:                                         # finally независимое выполнение
        print('завершение ')
