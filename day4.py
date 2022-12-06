from puzzle_input import read

data = read("input.txt", ['\n', ',', '-'])

total = 0
for line in data:
    if line[1][0] >= line[0][0] and line[1][1] <= line[0][1]: total += 1
    elif line[0][0] >= line[1][0] and line[0][1] <= line[1][1]: total += 1
print(total)

total = 0
for line in data:
    if line[0][1] >= line[1][0] and line[0][0] <= line[1][1]: total += 1
print(total)