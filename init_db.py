import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO MY_TABLE (val) VALUES ('Value 1')")
cur.execute("INSERT INTO MY_TABLE (val) VALUES ('Other Value')")
cur.execute("INSERT INTO MY_TABLE (val) VALUES ('3rd entry')")

connection.commit()
connection.close()
