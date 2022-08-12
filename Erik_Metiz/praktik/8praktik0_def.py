# 8.1
def display_message():
    print("i don't lave you")


display_message()


# 8.2
def favorite_book(book):
    print(f"One of my favorite books is {book.title()}")


favorite_book('lerning python ')


# 8.3
def make_shirt(size, text):
    print(f"Size own t-short: {size} and text on her: {text}")


make_shirt(44, 'i mudak')
make_shirt(size=56, text='faking human')


# 8.4
def make_shirt(size='L', text='«I love Python»'):
    print(f"Size own t-short: {size.title()} and text on her: {text}")


make_shirt()
make_shirt(size='m')


# 8.5
def describe_city(sity, country='russia'):
    print(f"{sity.title()} is in {country.title()}")


describe_city('podolsk')
describe_city('moscow')
describe_city('kiev', country='ukrain')


# 8.6
def city_country(sity, country):
    infirmation = f"{sity.title()} found in the country: {country.title()}"
    return infirmation


my_info = city_country('moscow', 'ru')
print(my_info)
print(city_country('santiago', 'chile'))


# 8.7

def make_album(name_musiant, name_albom, trek=''):
    if trek:
        oll_info = {'grupa': name_musiant, 'albom': {name_albom: trek}}
    else:
        oll_info = {'grupa': name_musiant, 'albom': name_albom}
    return oll_info


tarakan = make_album('tarakani', '21', 'kto-to iz nas dvoih')
print(tarakan)

print(f"\ngrupa {tarakan['grupa'].title()} albom {tarakan['albom']}")

nautilos = make_album('nautilos', 'fly')
print(nautilos)

for_9_may = make_album('for_9_may', 'ww2')
print(for_9_may)

# 8.7

def make_album(name_musiant, name_albom):
    oll_info = {'grup': name_musiant, 'albom': name_albom}
    return oll_info

while True:
    print(f"\nif you wont clouce thes ptogram enter: ss")
    name_grup = input("Please tell me grup:\n")
    if name_grup == 'ss':
        break
    name_albom = input("Please tell me albom:\n")
    if name_albom == 'ss':
        break

    the_your_rezult = make_album(name_grup,name_albom)
    print(the_your_rezult)
