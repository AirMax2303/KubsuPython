# import sqlite3
# import cgi
#
# #!/usr/bin/env python3
#
# print("Content-type: text/html")
# print("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
#     <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
# </head>
# <body>
#     <h4>Shop</h4>""")
#
# field_storage = cgi.FieldStorage()
#
# name = field_storage.getfirst("name")
#
# db = sqlite3.connect('photo-tech.db')
# sql = db.cursor()
#
# s = "select * from shop where name = ?"
# sql.execute(s, (name,))
#
# rows = sql.fetchall()
#
# for row in rows:
#     print(row[0])
#     print(row[1])
#     print(row[2])
#     print(row[3])
#
#
# print("""</body>
# </html>""")
#
# db.close()


import sqlite3
import cgi

#!/usr/bin/env python3

print("Content-type: text/html")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
<body>
    <h4>Shop</h4>""")

field_storage = cgi.FieldStorage()

name = field_storage.getfirst("name")
model = field_storage.getfirst("model")

db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

s = "select * from tech where name=? and model=?"
sql.execute(s, (name, model))

rows = sql.fetchall()

for row in rows:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print('\n')


print("""</body>
</html>""")

db.close()