a = []
print('Enter n: ')
n = int(input())

print('List input: ')
for i in range (n):
    elem = input().split()
    a.append(elem)

b = []
for i in range (len(a)):
    print(a.count(a[i])) 
    if a.count(a[i]) == 1:
        b.append(a[i])

print('List output: ')
print(b)

## Задание 14 Уникальные элементы. Дан список. Выведите те его
## элементы, которые встречаются в списке только один раз. Элементы нужно
## выводить в том порядке, в котором они встречаются в списке.