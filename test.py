# This space is just for chapter follow along and review exercises.
#

import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    results = cursor.execute(query)
    row = results.fetchone()
    time = row[0]
    print(time)
