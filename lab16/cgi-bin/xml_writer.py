import sqlite3
import xml.etree.ElementTree as ET

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
            </head>
            <body>""")

def write(dictionary, path):
    root = ET.Element('techs')

    for el in dictionary:
        sub1 = ET.SubElement(root, 'tech')
        sub20 = ET.SubElement(sub1, 'id')
        sub21 = ET.SubElement(sub1, 'name')
        sub22 = ET.SubElement(sub1, 'model')
        sub23 = ET.SubElement(sub1, 'address')
        sub24 = ET.SubElement(sub1, 'price')
        sub20.text = str(list(el.values())[0])
        sub21.text = str(list(el.values())[1])
        sub22.text = str(list(el.values())[2])
        sub23.text = str(list(el.values())[3])
        sub24.text = str(list(el.values())[4])

    tree = ET.ElementTree(root)
    tree.write(path, encoding='utf-8', xml_declaration=True)


conn = sqlite3.connect('photo-tech.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('select * from tech')

rows = []
for row in cursor.fetchall():
    rows.append(dict(row))

write(rows, 'tech_db.xml')

print("<h2>From DB to XML</h2>")
print(f'{rows}<br>')
print("<br>")
print("""<p><a href='/'>Back</a></p>""")
print("</body>")
print("</html>")