# with open ('file_st.txt', 'w', encoding = 'utf-8') as f:
#     while True:
#         stroka = input('Введите данные для записи ')
#         if stroka == '' or stroka.isspace():
#             print('запись окончена')
#             break
#         else:
#             f.writelines([stroka, '\\n'])
#             print(f'записал строку {stroka}')


# with open ('file_st.txt', 'r+', encoding = 'utf-8') as f:
#     for i, el in enumerate(f, 1):
#         print(f'строка№{i}, длина строки {len(el)}, {el}', end='')
#     t = f.tell()
#     print(f'\\nв файле было {i} строк(и)')
#     f.writelines(['Lilya\\n', '2109\\n', 'Python'])
#     print('Записались новые данные')
#     f.seek(t)
#     for i, el in enumerate(f, i + 1):
#         print(f'строка№{i}, длина строки {len(el)}, {el}', end='')

# from statistics import mean
# with open ('file_st.txt', 'r', encoding = 'utf-8') as f:
#     salary = []
#     for line in f:
#         salary.append(float(line.split()[1]))
#         if float(line.split()[1]) < 20000:
#             print(line, end='')
#     print(f'Средний доход сотрудников {mean(salary)}')

# dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# stroki = []
# with open ('file_1.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         stroka = dictionary[line.split()[0]] + line[len(line.split()[0]):]
#         stroki.append(stroka)
#         with open('file_2.txt', 'w', encoding='utf-8') as f1:
#             f1.writelines(stroki)

# with open ('file_3.txt', 'w', encoding = 'utf-8') as f:
#     ls = input('Введите набор чисел через пробел ')
#     f.write(ls)
#     print(sum(list(map(int, ls.split()))))

# ls_key = []
# ls_N = []
# with open ('file_4.txt', 'r', encoding = 'utf-8') as f:
#     for line in f:
#         ls_key.append(line.split()[0][:-1])
#         n = 0
#         for i in line.split():
#             if '(' in i:
#                 n = n+int(i.split('(')[0])
#             ls_N.append(n)
# dict_ls = dict(zip(ls_key, ls_N))
# print(dict_ls)



