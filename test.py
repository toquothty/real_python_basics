# This space is just for chapter follow along and review exercises.
#

import sqlite3


values = (
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29),
)

with sqlite3.connect("Roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute(
        """
    CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        Age INT
    );"""
    )

    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)
    cursor.execute(
        "UPDATE Roster SET Name=? WHERE Species=? and Age=?;",
        ("Ezri Dax", "Bajoran", 29),
    )

    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';")
    for row in cursor.fetchall():
        print(row)
