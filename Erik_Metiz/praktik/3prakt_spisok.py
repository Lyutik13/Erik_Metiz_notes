my_frend_and = ['Diman', 'Iliya', 'Rostov', 'Galya']
print(my_frend_and)
print(len(my_frend_and), 'гостя запланированно!')
print(f"он не сможет прийти: {my_frend_and[1].title()}")

new_fr = 'Yamyar'
my_frend_and[1] = new_fr
print(my_frend_and)
print("прийдёт:", new_fr)

for spisik in my_frend_and:
    print('прийдёт:', spisik, "!")
print("Придут новые гости")

my_frend_and.append('Misha')
my_frend_and.insert(0, 'Forest')
print(my_frend_and)
my_frend_and.insert(4, 'Tula')
print(my_frend_and)

for spisik in my_frend_and:
    print('прийдёт:', spisik, "!")

print("Ребята пизда всего 2 места")
print(my_frend_and)
print(f"он не сможет прийти: {my_frend_and[-1]}")
my_frend_and.pop()

print(my_frend_and)
print(f"он не сможет прийти: {my_frend_and[-1]}")
my_frend_and.pop()

print(my_frend_and)
print(f"он не сможет прийти: {my_frend_and[-1]}")
my_frend_and.pop()

print(my_frend_and)
print(f"он не сможет прийти: {my_frend_and[-1]}")
my_frend_and.pop()

print(my_frend_and)
print(f"он не сможет прийти: {my_frend_and[-1]}")
my_frend_and.pop()
print(my_frend_and)

print(f"ты приглашён: {my_frend_and[-1]}")
print(f"ты приглашён: {my_frend_and[0]}")

del my_frend_and[0]
del my_frend_and[0]
print(my_frend_and)


