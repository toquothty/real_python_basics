# This space is just for chapter follow along and review exercises.
#

from pathlib import Path
import csv

# Review Exercise 1
# file_path = Path.home() / "numbers.csv"

# numbers = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

# with file_path.open(mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(numbers)

# ////////////////////////////////////////////////////////////////////////////

# Review Exercise 2
# file_path = Path.home() / "numbers.csv"

# numbers = []

# with file_path.open(mode="r", encoding="utf-8", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         int_row = [int(value) for value in row]
#         numbers.append(int_row)
# print(numbers)

# //////////////////////////////////////////////////////////////////////////

# Review Exercise 3

# file_path = Path.home() / "favorite_colors.csv"

# favorite_colors = [
#     {"name": "Joe", "favorite_color": "blue"},
#     {"name": "Anne", "favorite_color": "green"},
#     {"name": "Bailey", "favorite_color": "red"},
# ]

# with file_path.open(mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
#     writer.writeheader()
#     writer.writerows(favorite_colors)

# /////////////////////////////////////////////////////////////////////////

# Review Exercise 4

file_path = Path.home() / "favorite_colors.csv"

favorite_colors = []

with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        favorite_colors.append(row)
print(favorite_colors)
