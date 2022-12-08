from array import *
from collections import Counter


def freqWord(t):
    return sorted((x for x in Counter(t).items()), key=lambda x: (-x[1], x[0]))[0][0]


wordBook = []

n = (int(input('Введите количество слов: ')))
for i in range(n):
    wordBook.append(input())
x = freqWord(wordBook)

print('Самое частое слово: ', x)


# Задание 4 Самое частое слово. Дан текст: в первой строке задано число
# строк, далее идут сами строки. Выведите слово, которое в этом тексте
# встречается чаще всего. Если таких слов несколько, выведите то, которое
# меньше в лексикографическом порядке.
