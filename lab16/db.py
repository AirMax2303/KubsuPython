import sqlite3

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

sql.execute("""create table tech (
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


db.commit()