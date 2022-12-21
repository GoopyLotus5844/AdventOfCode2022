from puzzle_input import read

data = read("input.txt", ['\n', ','])
data = set([tuple(item) for item in data])
disp = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

def in_range(pos):
    return -1 <= pos <= 20

def neighbors(loc):
    result = []
    for offset in disp:
        neighbor = (loc[0] + offset[0], loc[1] + offset[1], loc[2] + offset[2])
        if in_range(neighbor[0]) and in_range(neighbor[1]) and in_range(neighbor[2]):
            result.append(neighbor)
    return result

def flood_fill():
    start = (0, 0, 0)
    agenda = [start]
    found = {start}
    while agenda:
        loc = agenda.pop(0)
        for neighbor in neighbors(loc):
            if neighbor not in found and neighbor not in data:
                found.add(neighbor)
                agenda.append(neighbor)
    return found

sum = 0
for c in data:
    for d in disp:
        p = (c[0] + d[0], c[1] + d[1], c[2] + d[2])
        if not p in data: sum += 1
print(sum)

found = flood_fill()
sum = 0
for c in data:
    for d in disp:
        p = (c[0] + d[0], c[1] + d[1], c[2] + d[2])
        if p in found: sum += 1

print(sum)