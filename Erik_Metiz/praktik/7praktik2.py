# 7.8
sandwich_orders = ['cezar', 'mini', 'longer', 'big Rostov']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop(0)
    print(f"I made your {finished_sandwiche.title()}")
    finished_sandwiches.append(finished_sandwiche)

print("Oun sandwiches:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

# 7.9
sandwich_orders = ['big Rostov', 'cezar', 'mini', 'big Rostov', 'longer', 'big Rostov']
print(sandwich_orders)
while 'big Rostov' in sandwich_orders:
    sandwich_orders.remove('big Rostov')
print(sandwich_orders)

# 7.10
oprossnik = {}
next_or_stop = True

while next_or_stop:
    name = input("\nWhat is your name?\n")
    cauntry = input("What your favorite counry\n")
    oprossnik[name] = cauntry

#    ----------------------------------- stop while start -----------------------------------
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        next_or_stop = False
#    ------------------------------------ stop while end ------------------------------------

print("\n---Oтпрос завершен---")
for name, cauntry in oprossnik.items():
    print(f"{name.title()} favorite counry - {cauntry}")
print(oprossnik)
