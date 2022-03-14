import sqlite3

conn = sqlite3.connect("paskaita.db")

c = conn.cursor()


with conn:
    c.execute(""" CREATE TABLE IF NOT EXISTS paskaitos (pavadinimas text, destytojas text, trukme integer)""")
    c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40)")
    c.execute("INSERT INTO paskaitos VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO paskaitos VALUES ('Java', 'Tomas', 80)")
    c.execute("SELECT * FROM paskaitos WHERE trukme = 80")
    c.execute("UPDATE paskaitos SET pavadinimas='Python programavimas' WHERE pavadinimas='Python'")
    c.execute("DELETE FROM paskaitos WHERE destytojas = 'Tomas'")
    c.execute("SELECT * FROM paskaitos")
    print(c.fetchall())
