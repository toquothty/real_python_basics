# https://adventofcode.com/2021/day/1

# Count the number of times a depth measurement increases from the previous measurement.


increased_lines = 0
new_line = 0
with open('D1_Input.txt') as input:
    for line in input:
        line = int(line)
        if line > new_line:
            increased_lines += 1
            new_line = line
            print(f"{new_line} (increased)")
        else:
            new_line = line
            print(f"{new_line} (decreased)")

increased_lines = increased_lines - 1
print(f"The total increased lines are: {increased_lines}")


