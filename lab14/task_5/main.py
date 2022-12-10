'''Задание 5. Разработать программу со следующим графическим интерфейсом,предусмотреть обработку возможных ошибок.'''

from tkinter import *

root = Tk()
root.title("Программа для вычисления объёма сферы")
root.geometry('400x150')

Label(text="Имя:") \
    .grid(row=0, column=0)
Entry(width=30) \
    .grid(row=0, column=1, columnspan=3)

Label(text="Столбцов:") \
    .grid(row=1, column=0)
Spinbox(width=7, from_=1, to=50) \
    .grid(row=1, column=1)
Label(text="Строк:") \
    .grid(row=1, column=2)
Spinbox(width=7, from_=1, to=100) \
    .grid(row=1, column=3)

Button(text="Справка").grid(row=2, column=0)
Button(text="Вставить").grid(row=2, column=2)
Button(text="Отменить").grid(row=2, column=3)

root.mainloop()

'''from tkinter import *
import datetime

now = datetime.datetime.now()

root = Tk()
root.title("Sphere calc")
root.geometry('400x150')
lbl = Label(text="Введите текст:", font=("Arial Bold", 10))
lbl.pack()
text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()
Button(frame, text="В HTML").pack(side=LEFT)
Button(frame, text="В TXT").pack(side=LEFT)

root.mainloop()'''
