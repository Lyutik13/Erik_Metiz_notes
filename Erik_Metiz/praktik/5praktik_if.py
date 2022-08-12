# 5.3
alien_color = 'red'
if 'red' in alien_color:
    print('+5 очков')

if 'red' not in alien_color:
    print('no')
# 5.4
if 'green' in alien_color:
    print('+5 очков')
else:
    print('+10 очков')

if 'green' not in alien_color:
    print('+5 очков\n________________')
else:
    print('+10 очков')
# 5.5
if 'green' in alien_color:
    print('+ 5 очков')
elif 'red' in alien_color:
    print('+ 10 очков')
else:
    print('+15 очков')

# 5.6
age = 18
if age < 2:
    print('младенец')
elif age >= 2 and age < 4:
    print('малыш')
elif age >= 4 and age < 13:
    print('ребенок')
elif age >= 13 and age < 20:
    print('подросток')
elif age >= 20 and age < 65:
    print('взрослый')
else:
    print('пожилой человек')

# 5.7
favorite_fruits = ['apple', 'banana', 'dik', 'cheery']
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'orandge' in favorite_fruits:
    print('«You really like orandge!')
if 'dik' in favorite_fruits:
    print('«You really like dek!')
print('nace choice!')