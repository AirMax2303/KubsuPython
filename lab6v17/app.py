from array import *
import math

a = array('i',[])
b = int(input())
a.append(b)
while (b != 0):
    b = int(input())
    a.append(b)

su = 0
for i in range(0, len(a) - 1):
    su += a[i]
s = su//len(a)

su2 = 0
for i in range(0, len(a) - 1):
    su2 += (a[i] - s) * (a[i] - s)
auf = math.sqrt(su2/len(a) - 1)

print('Стандартное отклонение равно: ' and auf)


## Задание 17. 