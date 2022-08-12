#5.8
hello_admins = ['admin', 'Vitya', 'pidor', 'Niki', 'worker']
for hello_admin in hello_admins:
    if hello_admin == 'admin':
        print('Hello', hello_admin, 'would you like to see a status report?')
    else:
        print('Hello', hello_admin, 'thank you for logging in again')

#5.9
helllo_admins = []
if helllo_admins:
    print('hello', helllo_admins)
else:
    print('We need to ind some users!')

#5.10
current_users = ['admin', 'Vitya', 'pidor', 'Niki', 'worker', 'Galla']
lou_current_users = list(map(str.lower, current_users))   # новый список приведение к регистру
hi_current_users = list(map(str.upper, current_users))
tat_current_users = list(map(str.title, current_users))

new_users = ['Vitya', 'dima-dog', 'Niki', 'podsosi', 'gadi', 'galla']

for new_user in new_users:
    if new_user in lou_current_users:
        print('this name', new_user, 'is clouce for you')
    elif new_user in hi_current_users:
        print('this name', new_user, 'is clouce for you')
    elif new_user in tat_current_users:
        print('this name', new_user, 'is clouce for you')
    elif new_user in current_users:
        print('this name', new_user, 'is clouce for you')
    else:
        print(new_user, 'ok')
print(new_users)
print(lou_current_users)
print(hi_current_users)
print(tat_current_users)

# 5.11
int_name = list(range(1, 10))
print(int_name)
for name in int_name:
    if name == 1:
        print(name, 'st')
    elif name == 2:
        print(name, 'ed')
    elif name == 3:
        print(name, 'rd')
    else:
        print(name, 'th')

