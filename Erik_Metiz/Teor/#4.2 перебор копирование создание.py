players = ['charles', 'martina', 'michael', 'florence', 'eli']
# перебор части из списка
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Копирование списка
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  #тут

my_foods.append('ice-cream')
print("My favorite foods are:")
print(my_foods)

friend_foods.append('chiken')
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Создание сегмента
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('_____________________________________')
print(players[0:3])
print(players[1:4])
print(players[:4])