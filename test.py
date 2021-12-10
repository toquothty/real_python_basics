# This space is just for chapter follow along and review exercises.
#

from pathlib import Path

lines_of_text = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager\n"]

# path = Path.home() / "hello.txt"
# with path.open(mode="a", encoding="utf-8") as file:
#     file.writelines(lines_of_text)

# with path.open(mode="r", encoding="utf-8") as file:
#     for line in file.readlines():
#         print(line, end="")

path = Path.home() / "starships.txt"
with path.open(mode="w", encoding="utf-8") as file:
    file.writelines(lines_of_text)

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        if line[0] == "D":
            print(line, end="")
