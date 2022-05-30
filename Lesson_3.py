# def my_num(a, b):
#     if b == 0:
#         return
#     print(a / b)
# a = int(input('введите число a:'))
# b = int(input('введите число b:'))
# my_num(a, b)

# def my_data(em, sur, age, si, name, ph):
#     print(' '.join([name, sur, age, si, em, ph]))
# name = str(input('Введите имя:'))
# sur = str(input('Введите фамилию:'))
# age = str(input('Введите возраст:'))
# si = str(input('Ведите город проживания:'))
# em = str(input('Введите email:'))
# ph = str(input('Введите телефон:'))
# my_data(name = name, sur = sur, age = age, si = si, em = em, ph = ph)

# def my_func(a, b, c):
#     d = [a, b, c]
#     d.sort()
#     print(sum(d[1:]))
# a = int(input('введите a:'))
# b = int(input('введите b:'))
# c = int(input('введите c:'))
# my_func(a, b, c)

# def my_func(x, y):
#     print(x ** y)
# x =  int(input('введите x:'))
# y =  int(input('введите y, отрицательное:'))
# my_func(x, y)

# def my_func(x, y):
#     z = 1
#     while y < 0:
#         z = (1/x) * z
#         y = y + 1
#     print(z)
# x =  int(input('введите x:'))
# y =  int(input('введите y, отрицательное:'))
# my_func(x, y)

# i = 0
# y = 0
# u = True
# while u == True:
#     try:
#         sp = list(input('Введите числа через пробел').split())
#         for ei in range(len(sp)):
#             sp[ei] = int(sp[ei])
#             y = ei
#         i = sum(sp) + i
#         print(i)
#     except ValueError:
#         i = sum(sp[:y + 1]) + i
#         print(i)
#         u = False

# def int_func(sp):
#     for el in range(len(sp)):
#         sp[el] = sp[el].title()
#         print(sp[el] , end = " ")
# a = list(input('введите слова через пробел:').split())
# int_func(a)








