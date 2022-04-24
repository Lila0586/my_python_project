age = int(input('введите свой возраст'))
if age < 18:
    print('вход запрещен')
elif age == 18:
    print('Вам ровно 18')
else:
    print('вход разрешен')
    if age % 5 == 0:
        print('У вас юбилей!')
