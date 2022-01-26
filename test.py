# This space is just for chapter follow along and review exercises.
#

import sqlite3


sql = """
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    33
);"""

people_values = (
    ("Ron", "Obvious", 42),
    ("Luigi", "Vercotti", 43),
    ("Arthur", "Belling", 28),
)

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(sql)
    cursor.executemany("INSERT INTO People VALUES(?, ?, ?)", people_values)
