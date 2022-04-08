import sqlite3

conn = sqlite3.connect("darbuotojai (1).db")

c = conn.cursor()


c.execute("SELECT * FROM lentele")
c.execute("SELECT GIMIMO_DATA FROM lentele")
c.execute("SELECT VARDAS, PAVARDĖ, PAREIGOS FROM lentele")
c.execute("SELECT DISTINCT SKYRIUS_PAVADINIMAS FROM lentele")
c.execute("SELECT * FROM lentele WHERE SKYRIUS_PAVADINIMAS = 'Gamybos'")
c.execute("SELECT PAREIGOS FROM lentele WHERE VARDAS = 'Giedrius'")
c.execute("SELECT VARDAS, PAVARDĖ, PAREIGOS, SKYRIUS_PAVADINIMAS FROM lentele WHERE GIMIMO_DATA = '1986-09-19'")
c.execute("SELECT VARDAS, PAVARDĖ FROM lentele WHERE PAREIGOS = 'Programuotojas' AND SKYRIUS_PAVADINIMAS = 'Gamybos'")
c.execute("INSERT INTO lentele VALUES ('Rūta', 'Matonytė', '1997-07-20', 'Vadovė', 'Valdymas')")
c.execute("INSERT INTO lentele (VARDAS, PAVARDĖ, GIMIMO_DATA) VALUES ('Monika', 'Monikaitė', '1997-07-05')")
c.execute("UPDATE lentele SET PAREIGOS = 'Testuotojas', SKYRIUS_PAVADINIMAS = 'Gamybos' WHERE VARDAS = 'Monika' AND PAVARDĖ = 'Monikaitė'")
c.execute("DELETE FROM lentele WHERE GIMIMO_DATA = '1997-07-05'")
c.execute("DELETE FROM lentele WHERE GIMIMO_DATA = '1997-07-20'")
c.execute("INSERT INTO lentele (PAVARDĖ, PAREIGOS) VALUES ('Antanaitis', 'Programuotojas'")
c.execute("UPDATE lentele SET PAREIGOS='Programuotojas' WHERE PAREIGOS='Testuotojas'")
c.execute("SELECT count(*) FROM DARBUOTOJAI WHERE PAREIGOS = 'Testuotojas'")

print(c.fetchall())
