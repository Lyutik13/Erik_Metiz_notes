strani = ['Австралия', 'Япония', 'Чехия', 'Сирия', 'Норвегия', 'Вьетнам', 'Бразилия', 'Россия', 'USA']
print('1', strani)
print('2', sorted(strani))
print('3', strani)

print('4________________', sorted(strani, reverse=True), '_____________________')  # обратная без изменения
print('5', strani)

strani.reverse()
print('6', strani)
strani.reverse()
print('7', strani)

strani.sort()
print('8', strani)

strani.sort(reverse=True)
print('8',strani)
