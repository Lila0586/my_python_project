# from sys import argv
# time, sal, bonus = map(int, argv[1:])
# print(time*sal+bonus)

# new_sp = [int(input('введите элемент списка:')) for el in range(10)]
# new = [new_sp[el] for el in range(1, len(new_sp)) if new_sp[el] > new_sp[el - 1]]
# print(new)

# print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# sp = [int(input('Введите элемент списка:')) for el in range(10)]
# print(set(sp))

# from functools import reduce
# sp = [el for el in range(100, 1001 ) if el % 2 == 0]
# def umn(a , b):
#     return (a * b)
# print(reduce(umn, sp))

# from itertools import count, cycle
# sp = []
# for i in count(3):
#     sp.append(i)
#     print(i)
#     if i == 10:
#         break
# a = 0
# for i in cycle(sp):
#     print(i)
#     a += 1
#     if a == len(sp):
#         break

# def fact(n):
#     new = (i for i in range(1, n + 1))
#     for el in new:
#         yield el
#
# n = int(input('введите число:'))
# a = fact(n)
# for el in a:
#     print(el)




