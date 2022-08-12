for nombers in range(1, 21):
    print(nombers)
print("_______________________________________________________\n")

# milion = []
# for nombers_1 in range(1, 1000001):
#     milion.append(nombers_1)
# print(milion)
# print(min(milion), max(milion), sum(milion))

n_spis = []
for n_chet in range(1, 21, 2):
    n_spis.append(n_chet)
    print(n_chet)
print("________________________________________________________\n")

n_spis = []
for n_chet in range(3, 31, 3):
    n_spis.append(n_chet)
print(n_spis)

spis_3 = []
for nam_3 in range(1, 11):
    cub = nam_3**3
    spis_3.append(cub)
print(spis_3)

spis_3_1 =[value**3 for value in range(1, 11)]
print(spis_3_1)
