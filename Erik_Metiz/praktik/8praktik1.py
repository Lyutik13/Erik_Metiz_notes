# 8.9
short_messages = ['hi', 'bay', 'nace', 'oll pizda']


def show_messages(short_messages):
    for short_message in short_messages:
        print(short_message)


show_messages(short_messages)

# 8.10
short_messages = ['hi', 'bay', 'nace', 'oll pizda']
sent_messages = []


def show_messages(short_messages):
    print(f"\nInfo about mes:")
    for short_message in short_messages:
        print(short_message)


def send_messages(short_messages, sent_messages):
    while short_messages:
        one_short_messages = short_messages.pop()
        print(f"this mes del: {one_short_messages} !")
        sent_messages.append(one_short_messages)


show_messages(short_messages)
send_messages(short_messages, sent_messages)
print(short_messages)
print(sent_messages)
# ------------------------------------------ my test def --------------------------------------------
my_lisl = ['z', 'o', 'v']
my_mew_list = []

send_messages(my_lisl, my_mew_list)
show_messages(my_mew_list)
print(my_lisl)
print(my_mew_list)
my_mew_list.reverse()
print(my_mew_list)

# 8.11 save one list
myy_lisl = ['r', 'o', 'd', 'i', 'n', 'a']
myy_mew_list = []

send_messages(myy_lisl[:], myy_mew_list)

print(f"\nsave list:{myy_lisl} and new_list:{myy_mew_list}")
myy_mew_list.reverse()
print(myy_mew_list)


# 8.12
def sandvich(size, *ingreditnts):
    print(f"\nSandich {size} have a:")
    for ingreditnt in ingreditnts:
        print(ingreditnt)


sandvich(5, 'chees', 'free')


# 8.13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profil = build_profile('viktor'.title(), 'lyutikov'.title(),
                            location='m.o'.title())
print(user_profil)


# 8.14
def build_car(model, classs, **car_info):
    car_info['model_car'] = model
    car_info['classs'] = classs
    return car_info


oun_car = build_car('reno', 'sedan', winter_pakeige='no', musican='yes', color='grey')
print(oun_car)
