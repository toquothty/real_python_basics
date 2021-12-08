# https://adventofcode.com/2021/day/3

gamma_rate = []
epsilon_rate = []
# power_consumption = gamma_rate * epsilon_rate

#dictionary = ['A','B','C','D','E','F','G','H','I','J','K','L']

with open('D3_Input.txt') as input:
    for line in input:
        line_list = list(line)
        for n in range(0, len(line_list) - 1):
            for i in line_list[n]:
                print(i)
