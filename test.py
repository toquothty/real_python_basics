# This space is just for chapter follow along and review exercises.
#

from pathlib import Path
import csv


file_path = Path.home() / "employees.csv"


def process_row(row):
    row["salary"] = float(row["salary"])
    return row


with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(process_row(row))


people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 23},
]

file_path = Path.home() / "people.csv"
file = file_path.open(mode="w", encoding="utf-8", newline="")
writer = csv.DictWriter(file, fieldnames=["name", "age"])
writer.writeheader()
writer.writerows(people)
