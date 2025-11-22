import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Students;")
print(cursor.fetchall())

conn.close()
