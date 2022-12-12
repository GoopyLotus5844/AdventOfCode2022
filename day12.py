from puzzle_input import read
data = read("input.txt", ['\n'])

map = []
elev_a = []
for r, line in enumerate(data):
    if 'S' in line: 
        start = (r, line.index('S'))
        line = line.replace('S', 'a')
    if 'E' in line: 
        end = (r, line.index('E'))
        line = line.replace('E', 'z')
    map.append([ord(c) for c in line])

    for c, char in enumerate(line):
        if char == 'a': elev_a.append((r, c))

def neighbors(loc):
    result = []
    for offset in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        neighbor = (loc[0] + offset[0], loc[1] + offset[1])
        if neighbor[0] < 0 or neighbor[0] >= len(map) or neighbor[1] < 0 or neighbor[1] >= len(map[0]): continue
        if map[neighbor[0]][neighbor[1]] - map[loc[0]][loc[1]] <= 1: result.append(neighbor)
    return result

def solve(start):
    agenda = [(start, 1)]
    found = set()
    while agenda:
        loc = agenda.pop(0)
        for neighbor in neighbors(loc[0]):
            if neighbor not in found:
                if neighbor == end: return loc[1]
                found.add(neighbor)
                agenda.append((neighbor, loc[1] + 1))

print(solve(start))

lengths = []
for loc in elev_a:
    length = solve(loc)
    if length != None: lengths.append(length)

print(min(lengths))