# Перебор всего списка цыкл:  for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Более сложные действия в циклах for    (обращение через f к списку + сообщения с форматированием)
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# Выполнение действий после цикла for
print("Thank you, everyone. That was a great magic show!")



