import sqlite3

conn = sqlite3.connect('HOTDOGS.db')
c = conn.cursor()

c.execute("CREATE TABLE DOGGIES(id INTEGER PRIMARY KEY, size varchar(10), spicy bit, vegan bit, comment varchar(255))")

conn.commit()
conn.close()