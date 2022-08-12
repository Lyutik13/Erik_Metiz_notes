# 10.6 - 10.7
# while True:
#     try:
#         first_number = input("\nFirst number: \n")
#         if first_number == 'q':
#             break
#         second_number = input("Second number: \n")
#         if second_number == 'q':
#             break
#
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("Enter int!")
#     else:
#         print(answer)
#         break

# # 10.8
# def read_file(filename):
#     """читает содержимое файла и обрабатывает ошибку если его нет"""
#     try:
#         with open(filename, encoding='utf-8') as file_object:
#             content = file_object.read()
#     except FileNotFoundError:
#         pass
#         #print(f"Sorry, the file {filename} does not exist")
#     else:
#         my_list = content.split()
#         print(my_list)
#
#
# filenames = ['test_files/car.txt', 'test_files/dog.txt', 'sdfafgdffd']
# for filename in filenames:
#     read_file(filename)


# 10.10
filename = 'V:\\PycharmProjects\\lern\\Erik_Metiz\\Teor\\files\\moby_dick.txt'
with open(filename, "r", encoding="utf-8") as file_object:
    contents = file_object.read().lower().count('the ')
    print(contents)
