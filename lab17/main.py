import sqlite3

with sqlite3.connect("Pharmacy.db") as db:
    cursor = db.cursor()

