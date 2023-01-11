import sqlite3
import cgi

field_storage = cgi.FieldStorage()

name = field_storage.getfirst("name")
model = field_storage.getfirst("model")

db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

sql.execute(f"delete from tech where name=? and model=?", (name, model))
db.commit()