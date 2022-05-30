# '''Задание1'''
#
#
# class Matrix:
#     def __init__(self, spisokob):
#         self.sp = spisokob
#
#     def __str__(self):
#         s = ''
#         for i in range(len(self.sp)):
#             for j in range(len(self.sp[i])):
#                 s += f'{self.sp[i][j]} '
#             s += '\n'
#         return s
#
#     def __add__(self, other):
#         self.sp1 = self.sp
#         for i in range(len(self.sp)):
#             for j in range(len(self.sp[i])):
#                 self.sp1[i][j] = self.sp[i][j] + other.sp[i][j]
#         return Matrix(self.sp1)
#
#
# matrix1 = Matrix([[1, 2, 3], [3, 4, 3], [1, 2, 3]])
# matrix2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
# print(matrix1)
# print(matrix2)
# print(matrix1 + matrix2)

# '''Задание 2'''
# from abc import ABC, abstractmethod
#
#
# class Coat(ABC):
#     @abstractmethod
#     def __init__(self, v):
#         self.v = v
#
#     def ras_coat(self):
#         return self.v / 6.5 + 0.5
#
#
# class Suit(ABC):
#     @abstractmethod
#     def __init__(self, h):
#         self.h = h
#
#     def ras_suit(self):
#         return self.h * 2 + 0.5
#
#
# class Clothes(Coat, Suit):
#     def __init__(self, v, h):
#         self.v = v
#         self.h = h
#
#     @property
#     def volume(self):
#         return self.v
#
#     @volume.setter
#     def volume(self, v):
#         self.v = v
#
#     @property
#     def growth(self):
#         return self.h
#
#     @growth.setter
#     def growth(self, h):
#         self.h = h
#
#     def sum_ras(self):
#         return (self.v / 6.5 + 0.5) + (self.h * 2 + 0.5)
#
#
# razm = Clothes(103, 2)
# print(razm.sum_ras())
# print(razm.ras_coat())
# print(razm.ras_suit())
# razm.growth = 1.5
# razm.volume = 73
# print(razm.sum_ras())
# print(razm.ras_coat())
# print(razm.ras_suit())

#'''Задание 3'''
# class Cells:
#     def __init__(self, n):
#         self.n = n
#
#     def __add__(self, other):
#         return self.n + other.n
#
#     def __sub__(self, other):
#         if other.n > self.n:
#             return "Нельзя вычесть клетки!"
#         else:
#             return self.n - other.n
#
#     def __mul__(self, other):
#         return self.n * other.n
#
#     def __truediv__(self, other):
#         return self.n // other.n
#
#     def make_order(self):
#         s = ''
#         for i in range(1, self.n + 1):
#             if i % 5 == 0:
#                 s += '*\n'
#             else:
#                 s += '*'
#         return s
#
# cells = Cells(10)
# cells2 = Cells(1)
# cells3 = Cells(cells + cells2)
# # print(cells3.make_order())
# print(cells.make_order())
# print(cells2.make_order())
# print(cells + cells2)
# print(cells - cells2)
# print(cells / cells2)
# print(cells * cells2)
