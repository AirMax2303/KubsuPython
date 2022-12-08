n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)

for i in range(len(a)):
    x = a[i]
    y = a[:i]
    if x in y:
        print('YES')
    else:
        print('NO')