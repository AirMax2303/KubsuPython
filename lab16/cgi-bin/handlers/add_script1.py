import sqlite3
import cgi

field_storage = cgi.FieldStorage()

name = field_storage.getfirst("name")
country = field_storage.getfirst("country")
CEO = field_storage.getfirst("CEO")


db = sqlite3.connect('photo-tech.db')
sql = db.cursor()

sql.execute(f"insert into manufacturer (name, country, CEO) values (?, ?, ?)", (name, country, CEO))
db.commit()