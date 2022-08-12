######################################### Команда break #######################################
# смотри 7praktik1 while

# Чтобы немедленно прервать цикл while без выполнения оставшегося кода в цикле независимо от состояния условия

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)\n"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# --- Команда continue - продолжение цикла ---

################################# Использование цикла while со списками и словарями ################################

# -------------------------------- Перемещение элементов между списками --------------------------------

# Начинаем с двух списков: пользователей для проверки и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# ------------------------------ Удаление всех вхождений конкретного значения из списка ------------------------------

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# ------------------------------ Заполнение словаря данными, введенными пользователем ------------------------------

responses = {}

# Установка флага продолжения опроса.
polling_active = True


while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name?\n")
    response = input("Which mountain would you like to climb someday?\n")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
