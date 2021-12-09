# Chapter 12 Challenge: Move all image files to a new directory
# Create a images directory
# Move all images from documents to images directory
# png, gif, jpg

from pathlib import Path
import shutil

# Assign and create directory variable.
my_folder = Path.home() / "Python" / "python-basics-exercises-master" / "ch12-file-input-and-output" / "practice_files" / "images"
my_folder.mkdir(exist_ok=True)

iterate_folder = Path.home() / "Python" / "python-basics-exercises-master" / "ch12-file-input-and-output" / "practice_files"

# Loop through the known extension types and perform copies.
for file in list(iterate_folder.rglob("*.png")):
    destination = my_folder 
    dest = shutil.copy(file, destination)
for file in list(iterate_folder.rglob("*.gif")):
    destination = my_folder 
    dest = shutil.copy(file, destination)
for file in list(iterate_folder.rglob("*.jpg")):
    destination = my_folder 
    dest = shutil.copy(file, destination)

