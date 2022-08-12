my_fute = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print('Three items from the middle of the list are:')
print(my_fute[:3])
print(my_fute[1:4])
print(my_fute[-3:])

pizzas = ['pizza', 'falafel', 'carrot cake']
friend_pizzas = pizzas[:]
pizzas.append('macarela')
friend_pizzas.append('cezar')
print('My favorite pizzas are:', pizzas)
print('My friend’s favorite pizzas are:', friend_pizzas)

for pizza in pizzas:
    print(pizza)
print('___________________________________')

for f_p in friend_pizzas:
    print(f_p)