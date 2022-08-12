# если вы хотите, чтобы в программе выполнялся только один блок кода,
# используйте цепочку if-elif-else
age = 50

if age <= 4:
    price = 0
elif age <= 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print("Your admission cost is $", price)

# Если же выполняться должны несколько блоков,
# используйте серию независимых команд if.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
 print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
 print("Adding extra cheese.")

 print("\nFinished making your pizza!")

