BEGIN TRANSACTION;
DROP TABLE IF EXISTS "rules";
CREATE TABLE IF NOT EXISTS "rules" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "employees";
CREATE TABLE IF NOT EXISTS "employees" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"id_rule"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "sales_journal";
CREATE TABLE IF NOT EXISTS "sales_journal" (
	"sales_id"	INTEGER NOT NULL UNIQUE,
	"medicines_id"	INTEGER,
	"count"	INTEGER,
	"employees_id"	INTEGER,
	"time"	TEXT DEFAULT (datetime('now', 'localtime')),
	PRIMARY KEY("sales_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "storage";
CREATE TABLE IF NOT EXISTS "storage" (
	"id_medicines"	INTEGER,
	"price"	INTEGER,
	"count"	INTEGER,
	"date_add"	INTEGER
);
DROP TABLE IF EXISTS "medicines";
CREATE TABLE IF NOT EXISTS "medicines" (
	"medicines_id"	INTEGER,
	"name"	TEXT,
	"country"	TEXT,
	"date"	TEXT,
	"storage_life"	INTEGER,
	PRIMARY KEY("medicines_id")
);
COMMIT;
