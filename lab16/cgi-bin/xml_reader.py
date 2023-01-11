import sqlite3
import xml.dom.minidom as minidom

def get_data(dom):
    dictionary = {}
    value = []

    for elem in dom:
        for child in elem.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'id':
                    if child.firstChild.nodeType == 3:
                        key = int(child.firstChild.data)

                if child.tagName == 'name':
                    if child.firstChild.nodeType == 3:
                        value.append(str(child.firstChild.data))

                if child.tagName == 'model':
                    if child.firstChild.nodeType == 3:
                        value.append(str(child.firstChild.data))

                if child.tagName == 'address':
                    if child.firstChild.nodeType == 3:
                        value.append(str(child.firstChild.data))

                if child.tagName == 'price':
                    if child.firstChild.nodeType == 3:
                        value.append(int(child.firstChild.data))
                        
        dictionary[key] = value
        value = []
    return dictionary

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
            </head>
            <body>""")

datasource = open('tech_db.xml')
dom2 = minidom.parse(datasource)
dom2 = dom2.getElementsByTagName('tech')

dict = get_data(dom2)

item_list = []
for key, value in dict.items():
   item_list.append((key, str(value[0]), str(value[1]), str(value[2]), int(value[3])))

db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

sql.execute("""create table if not exists shop (
    id integer primary key autoincrement,
    name text not null,
    address text not null,
    status text not null
)""")

sql.execute("""create table if not exists manufacturer (
    id integer primary key autoincrement,
    name text not null,
    country text not null,
    CEO text not null
)""")

sql.execute("""create table if not exists tech (
    id integer primary key autoincrement,
    name text not null,
    model text not null,
    address text not null,
    price integer not null,
    foreign key (name)
        references manufacturer (name),
    foreign key (address)
        references shop (address)
)""")

sql.executemany('''
    INSERT or replace INTO tech (id, name, model, address, price) VALUES (?, ?, ?, ?, ?)
''', item_list)

db.commit()
db.close()
print("<h2>Records main table</h2>")
print(f'{item_list}<br>')
print("<br>")
print("""<p><a href='/'>Back</a></p>""")
print("</body>")
print("</html>")