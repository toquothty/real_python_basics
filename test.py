# This space is just for chapter follow along and review exercises.
#

import sqlite3

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()

query = "SELECT datetime('now', 'localtime');"
results = cursor.execute(query)

row = results.fetchone()
print(row)

connection.close()
