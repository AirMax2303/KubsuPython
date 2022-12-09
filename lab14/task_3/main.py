"""Задание 3*. Напишите программу, которая позволяет произвольный 
текст, введенный с клавиатуры, по нажатию кнопки сохранить в обычный 
текстовый файл либо в файл HTML-формата (тип файла указывается с 
помощью выпадающего меню)."""
from tkinter import *
import datetime

now = datetime.datetime.now()


def translate_to_html():
    _name_files = str(now.date()) + "-" + str(now.time())[0:5].replace(":", "-")
    with open(f"result/{_name_files}.html", "w") as r:
        html_top = """
        <html>
          <head>
           <meta http-equiv="Content-Type" content="text/html">
           <title>Пример веб-страницы</title>
         </head>
         <body>
         <h1>"""
        html_bottom = """
        </h1>
        </body>
        </html>
        """
        r.write(html_top + text.get(1.0, END) + html_bottom)
        print(str(now.date()))


def translate_to_txt():
    _name_files = str(now.date()) + "-" + str(now.time())[0:5].replace(":", "-")
    with open(f"result/{_name_files}.txt", "w") as r:
        r.write(text.get(1.0, END))
        print()


root = Tk()
root.title("Text translator by Maxim Lysenko")
root.geometry('400x150')
lbl = Label(text="Введите текст:", font=("Arial Bold", 10))
lbl.pack()
text = Text(width=25, height=5)
text.pack()

frame = Frame()
frame.pack()
Button(frame, text="В HTML",
       command=translate_to_html).pack(side=LEFT)
Button(frame, text="В TXT",
       command=translate_to_txt).pack(side=LEFT)

root.mainloop()
