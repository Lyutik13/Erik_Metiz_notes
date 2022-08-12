# # 7.4  Выход из цикла по команде break

# add_top = []
#
# while True:
#     messedge = "какой топинг добпвить?\n"
#     topping = input(messedge)
#     if topping == 'stop':
#         break
#     else:
#         print('хотите ещё?')
#         add_top.append(topping)
#         print(add_top)

# # 7.4.1  Завершение цикла по проверке условия в команде while.

# add_top = []
# enter = "какой топинг добпвить?\n"
# messedge = ""
# while messedge != 'stop':
#     messedge = input(enter)
#     add_top.append(messedge)
#     print(add_top)

# 7.4.2  Управление продолжительностью выполнения цикла в зависимости от переменной active

# add_top = []
# active = True
# while active:
#     messedge = "какой топинг добпвить?\n"
#     topping = input(messedge)
#     if topping == 'stop':
#         active = False
#     else:
#         print('хотите ещё?')
#         add_top.append(topping)
#         print(add_top)

# 7.5

while True:
    age = int(input("Entering your age\n"))
    if age <= 2:
        print("Free")
    elif age >= 3 and age <= 12:
        print("$10")
    else:
        print("$15")

