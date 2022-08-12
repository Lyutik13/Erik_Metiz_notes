# 10.3
# filename = 'test_files/quest.txt'
# name_user = input(f"Pleace enter your name :\n")
#
# with open(filename, 'w') as file_object:
#     file_object.write(name_user)

# 10.4
filename1 = 'test_files/guest_book.txt'
while True:
    your_name = input("Entering your name:\n")
    if your_name == 'stop':
        break
    print(f"Hello {your_name}\nYou were wrote.")
    with open(filename1, 'a') as file_object1:
        file_object1.write(your_name)
        file_object1.write("\n")

# 10.5
filename2 = 'test_files/riran10.5.txt'
while True:
    rizan = input("why do you like programing?\n")
    if rizan == 'stop':
        break
    print(f"nice, save!")
    with open(filename2, 'a') as file_object2:
        file_object2.write(rizan)
        file_object2.write("\n")
