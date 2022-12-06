from puzzle_input import read
data = read("input.txt", ['\n', ' '])

score = 0
for line in data:
    if line[1] == 'X':
        if line[0] == 'C': score += 6
        elif line[0] == 'A': score += 3
        score += 1
    if line[1] == 'Y':
        if line[0] == 'A': score += 6
        elif line[0] == 'B': score += 3
        score += 2
    if line[1] == 'Z':
        if line[0] == 'B': score += 6
        elif line[0] == 'C': score += 3
        score += 3

print(score)

score = 0
for line in data:
    if line[1] == 'X':
        if line[0] == 'A': score += 3
        elif line[0] == 'B': score += 1
        else: score += 2
    if line[1] == 'Y':
        if line[0] == 'A': score += 1
        elif line[0] == 'B': score += 2
        else: score += 3
        score += 3
    if line[1] == 'Z':
        if line[0] == 'A': score += 2
        elif line[0] == 'B': score += 3
        else: score += 1
        score += 6

print(score)

