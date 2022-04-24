# name = 43
# li = ['555', '123', 666, 'Alex', name]
# # for i in range(5):
# #     print(type(li[i]))
# # li[0], li[1] = li[1], li[0]
# # li[2], li[3] = li[3], li[2]
# # print(li)
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# li = list(input('введите данные через запятую').split(','))
# for i in range(0,len(li)-1, 2):
#     li[i], li[i+1] = li[i+1], li[i]
#     print(li)

# month = int(input('Введите месяц  от 1 до 12: '))
# dictionary = {'зима' : [12,1,2], 'весна': [3,4,5], 'лето': [6,7,8], 'осень': [9,10,11]}
# for i in dictionary:
#     if month in dictionary[i]:
#         print(i)
# st = list(input ('Введите список элементов через пробел ').split())
# for i,el in enumerate(st[:10], 1):
#     print(i, el)
li = [7, 5, 3, 3, 2]
li2 = int(input('Введите новый элемент: '))
li.append(0)
for i in range(len(li)):
    if li[i] < li2:
     li.insert(i,li2)
     break
li.pop(-1)
print(li)













