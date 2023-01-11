import sqlite3
import cgi

field_storage = cgi.FieldStorage()

name = field_storage.getfirst("name")
address = field_storage.getfirst("address")
status = field_storage.getfirst("status")


db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

sql.execute(f"insert into shop (name, address, status) values (?, ?, ?)", (name, address, status))
db.commit()