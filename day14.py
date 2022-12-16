from puzzle_input import read

data = read("input.txt", ['\n', '->', ','])

size = 800
grid = [['.'] * size for i in range(size)]

for path in data:
    for i in range(len(path) - 1):
        one = path[i]
        two = path[i + 1]
        if one[0] == two[0]:
            for x in range(min(one[1], two[1]), max(one[1], two[1]) + 1): grid[x][one[0]] = '#'
        else:
            for x in range(min(one[0], two[0]), max(one[0], two[0]) + 1): grid[one[1]][x] = '#'

max_y = 0
for path in data:
    for point in path:
        if point[1] > max_y: max_y = point[1]
floor = max_y + 2

for i in range(size):
    grid[floor][i] = '#'

def print_grid(grid):
    for line in grid[:10]:
        print(''.join(line[490:]))

running = True

def get(loc):
    if loc[0] < 0 or loc[0] >= size or loc[1] < 0 or loc[1] >= size: return '#'
    return grid[loc[1]][loc[0]]

count = 0
while running:
    sand = [500, 0]
    while True:
        next = [sand[0], sand[1] + 1]

        if get(next) == '.':
            sand = next
        elif get([next[0] - 1, next[1]]) == '.':
            sand = [next[0] - 1, next[1]]
        elif get([next[0] + 1, next[1]]) == '.':
            sand = [next[0] + 1, next[1]]
        else:
            if sand == [500, 0]: 
                print(count)
                running = False
            grid[sand[1]][sand[0]] = 'O'
            break
    count += 1

