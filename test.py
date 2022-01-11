# This space is just for chapter follow along and review exercises.
#

from pathlib import Path
import csv


# daily_temperatures = [
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73],
# ]

daily_temperatures = []

file_path = Path.home() / "temperatures.csv"
# with file_path.open(mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(daily_temperatures)


with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        daily_temperatures.append(int_row)


print(daily_temperatures)
