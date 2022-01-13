# Chapter 12 Challenge: Create a High Scores List
#
# Read in data from practice file: scores.csv
# Create new file in which each row contains player's name and score

from pathlib import Path
import csv
from types import prepare_class

scores = (
    Path.home()
    / "Python"
    / "python-basics-exercises-master"
    / "ch12-file-input-and-output"
    / "practice_files"
    / "scores.csv"
)

high_scores = Path.home() / "high_scores.csv"

process_scores = []


def process_row(row):
    row["score"] = int(row("score"))
    return row


with scores.open(mode="r", encoding="utf-8", newline="") as source_file:
    reader = csv.DictReader(source_file)
    for row in reader:
        process_scores.append(row)

with high_scores.open(mode="w", encoding="utf-8", newline="") as dest_file:
    writer = csv.DictWriter(dest_file, fieldnames=process_scores[0].keys())
    writer.writeheader()
    writer.writerows(process_scores)
