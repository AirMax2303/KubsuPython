from array import *
import re

a = []  # Список для построчного записывания файла

fname = input('Введите имя файла: ')
f = open(fname, 'r')
a = f.readlines()
for i in range(len(a)):
    a[i] = a[i].strip()
print('Имя файла: ' + fname)
for i in range(len(a)):
    if "def " in a[i]:
        if "##" not in a[i - 1]:
            print('Номер строки: ' + str(i) + '; Имя функции: ' +
                  re.search('def ([a-zA-Z_]+)', a[i]).group(1))
