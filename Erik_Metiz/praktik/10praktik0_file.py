# 10.1
# с чтением всего файла
with open('test_files/learn_py.txt') as learn_objects:
    contents = learn_objects.read()
    print(contents)

# Чтение по строкам
with open('test_files/learn_py.txt') as learn_objects:
    for line in learn_objects:
        print(line)

# Создание списка строк по содержимому файла
with open('test_files/learn_py.txt') as learn_objects:
    learn_lists = learn_objects.readlines()

print(learn_lists)
for liiist in learn_lists:
    print(liiist.strip())

# 10.2 replace()
print(f"______________________________________________________________________________")
with open('test_files/learn_py.txt') as learn_objects1:
    learn_objects1 = learn_objects1.readlines()

str_lern_obj = ''
for line1m in learn_objects1:
    str_lern_obj += line1m

a = str_lern_obj.replace('Python', 'C')
print(a)
