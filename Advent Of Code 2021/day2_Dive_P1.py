# https://adventofcode.com/2021/day/2

depth_position = 0
horizontal_position = 0

with open('D2_Input.txt') as input:
    for line in input:
        key, value = line.split()
        if key == 'forward':
            horizontal_position = horizontal_position + int(value)
        #    print(horizontal_position)
        elif key == 'down':
            depth_position = depth_position + int(value)
        else:
            depth_position = depth_position - int(value)

print(f"The final depth_position is {depth_position}")
print(f"The final horizontal position is {horizontal_position}")

final_position = depth_position * horizontal_position

print(f"The final position is {final_position}")