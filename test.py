# This space is just for chapter follow along and review exercises.
#

from pathlib import Path

lines_of_text = ["Hello on line 1\n", "Hello on line 2\n", "wiggida\n"]

path = Path.home() / "hello.txt"
with path.open(mode="a", encoding="utf-8") as file:
    file.writelines(lines_of_text)

with path.open(mode="r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
