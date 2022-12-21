import sqlite3


def insertData():
    cursor.execute("""
INSERT INTO "rules" ("id","name") VALUES
 (1,'Директор аптечной организации'),
 (2,'Заместитель директора аптечной организации'),
 (3,'Заведующий структурного подразделения аптечной организации'),
 (4,'Провизор-технолог'),
 (5,'Заведующий структурного подразделения'),
 (6,'Провизор-аналитик'),
 (7,'Провизор'),
 (8,'Фармацевт'),
 (9,'Младший фармацевт'),
 (10,'Старший фармацевт'),
 (11,'Работник склада');
        """)
    cursor.execute("""
INSERT INTO "employees" ("id","name","id_rule") VALUES
 (1,'Петров Дмитрий Владимирович',1),
 (2,'Афанасьев Анальгин Петрович',2),
 (3,'Горбачёв Андрей Евгеньевич',5),
 (4,'Говрированный Максим Владимирович',8),
 (5,'Афанасьев Игорь Петрович',10),
 (6,'Петров Гавриил Александрович',4),
 (7,'Спиралька Алла Русамовна',8),
 (8,'Богданова Алёна Максимовна',9),
 (9,'Василисова Василиса Васильевна',6),
 (10,'Петров Семён Антонович',10);
        """)
    cursor.execute("""
INSERT INTO "sales_journal" ("sales_id","medicines_id","count","employees_id","time") VALUES
 (1,4,20,7,'2022-12-20 19:26:15'),
 (2,10,1,7,'2022-12-20 19:26:15'),
 (3,11,2,7,'2022-12-20 19:26:15'),
 (4,6,10,4,'2022-12-20 19:26:15'),
 (5,3,7,7,'2022-12-20 19:26:15'),
 (6,4,2,7,'2022-12-20 19:26:15'),
 (7,1,1,4,'2022-12-20 19:26:15'),
 (8,2,5,4,'2022-12-20 19:26:15'),
 (9,9,4,7,'2022-12-20 19:26:15'),
 (10,2,5,4,'2022-12-20 19:26:15'),
 (11,5,5,4,'2022-12-20 19:26:15');
        """)
    cursor.execute("""
INSERT INTO "storage" ("id_medicines","price","count","date_add") VALUES
 (2,111,80,'05.06.2001'),
 (6,222,36,'05.06.2001'),
 (2,2462,31,'05.06.2001'),
 (5,2623,135,'05.06.2001'),
 (4,135,153,'05.06.2001'),
 (2,153,673,'05.06.2001'),
 (1,484,22,'05.06.2001'),
 (7,3636,252,'05.06.2001'),
 (11,422,1346,'05.06.2001');
        """)
    cursor.execute("""
INSERT INTO "medicines" ("medicines_id","name","country","date","storage_life") VALUES
 (1,'Амбросол','Польша','23.07.2001',24),
 (2,'Аскофен','Россия','24.11.2001',36),
 (3,'Аспирин','Польша ','25.07.2002',36),
 (4,'Бисептол','Индия','26.07.2000',24),
 (5,'Фервекс','Россия','27.07.2000',24),
 (6,'Бесалол','Россия','05.06.2001',36),
 (7,'Валидол','Россия','29.12.2001',36),
 (8,'Мукалтин','Индия ','02.03.2001',36),
 (9,'Дексалгин','Россия','08.07.2002',36),
 (10,'Солпадеин','Польша','01.06.2002',24),
 (11,'Колдрекс','Россия','02.08.2001',36),
 (12,'Нурофен','Россия','04.04.2000',36),
 (13,'Панадол','Индия','15.05.2002',24),
 (14,'Анальгин','Россия','26.07.2002',24),
 (15,'Супрастин','Россия','19.06.2001',36);
        """)


with sqlite3.connect("Pharmacy.db") as db:
    cursor = db.cursor()
    with open('Pharmacy.sql', 'r') as f:
        cursor.executescript(f.read())
        insertData()
        db.commit()
        cursor.execute("""
        SELECT
	sales_journal.sales_id,
	employees.name, 
	medicines.name,
	sales_journal.count,
	sales_journal.time
FROM sales_journal
LEFT JOIN employees on employees.id = sales_journal.employees_id
LEFT JOIN medicines on medicines.medicines_id = sales_journal.medicines_id
                """)
        print('-------------------------------------------------')
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4], "\n")
        print('-------------------------------------------------')
        print('table: employees')
        cursor.execute("""SELECT * FROM employees""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], ' ', row[2], "\n")
        print('-------------------------------------------------')
        print('table: medicines')
        cursor.execute("""SELECT * FROM medicines""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4], "\n")
        print('-------------------------------------------------')
        print('table: rules')
        cursor.execute("""SELECT * FROM rules""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        print('table: sales_journal')
        cursor.execute("""SELECT * FROM sales_journal""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], ' ', row[4], "\n")
        print('-------------------------------------------------')
        print('table: storage')
        cursor.execute("""SELECT * FROM storage""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], "\n")
        print('-------------------------------------------------')
        cursor.execute("""SELECT storage.id_medicines, storage.count FROM storage""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        cursor.execute("""SELECT storage.id_medicines,storage.date_add FROM storage""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        cursor.execute("""SELECT medicines.name, medicines.country FROM medicines""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        cursor.execute("""SELECT medicines.name, medicines.storage_life FROM medicines""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        cursor.execute("""SELECT medicines.name, medicines.date FROM medicines""")
        records = cursor.fetchall()
        for row in records:
            print(row[0], ' ', row[1], "\n")
        print('-------------------------------------------------')
        cursor.execute("""
        UPDATE employees
        SET id_rule = 3
        WHERE id_rule = 2
        """)
        cursor.execute("""
        UPDATE employees
        SET id_rule = 4
        WHERE id_rule = 2
        """)
        cursor.execute("""
        UPDATE medicines
        SET storage_life = 30
        WHERE medicines_id = 2
        """)
        cursor.execute("""
        UPDATE storage
        SET count = count - 1
        WHERE id_medicines = 1
        """)
        cursor.execute("""
        UPDATE storage
        SET count = count - 1
        WHERE id_medicines = 5
        """)
        cursor.execute("""
        UPDATE storage
        SET count = count - 4
        WHERE id_medicines = 11
        """)
        cursor.execute("""
        DELETE FROM sales_journal
        WHERE sales_id = 9;
        """)
