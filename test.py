# This space is just for chapter follow along and review exercises.
#

from pathlib import Path
import shutil

my_folder = Path.home() / "my_folder"
my_folder.mkdir(exist_ok=True)


paths = [
    my_folder / "file1.txt",
    my_folder / "file2.txt",
    my_folder / "image1.png"
]

for path in paths:
    path.touch()

source = my_folder / "image1.png"
destination = my_folder / "images" / "image1.png"

images = Path.home() / "my_folder" / "images"
images.mkdir(exist_ok=True)

source.replace(destination)

del_file = my_folder / "file1.txt"
del_file.unlink()

del_structure = my_folder
shutil.rmtree(del_structure)