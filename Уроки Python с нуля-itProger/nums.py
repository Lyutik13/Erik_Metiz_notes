# nums = [5, 2, 7, '50', False]
#
# for i in nums:
#     i *= 10
#     print(i)

spis = int(input('Enter:\n '))

list_ = []

i = 0

while i < spis:
    string = 'Введёная хрень № ' + str(i + 1) + ':'
    list_.append(input(string))
    i += 1

print(list_)
