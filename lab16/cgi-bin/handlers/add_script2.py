import sqlite3
import cgi

field_storage = cgi.FieldStorage()

name = field_storage.getfirst("name")
model = field_storage.getfirst("model")
address = field_storage.getfirst("address")
price = int(field_storage.getfirst("price"))


db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

sql.execute(f"insert into tech (name, model, address, price) values (?, ?, ?, ?)", (name, model, address, price))
db.commit()