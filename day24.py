from puzzle_input import read

data = read("input.txt", ['\n'])

grid = [[[c] if c != '.' else [] for c in row[1:-1]] for row in data[1:-1]]
grids = [grid]
depth = 2000

start = (-1, 0)
dest = (len(grid), len(grid[0]) - 1)

def disp(grid):
    for row in grid:
        print(''.join((blizzard[0] if len(blizzard) == 1 else str(len(blizzard))) if len(blizzard) > 0 else '.' for blizzard in row))

def move_dir(pos, char, dim):
    if char == '>': new_pos = (pos[0], pos[1] + 1)
    elif char == 'v': new_pos = (pos[0] + 1, pos[1])
    elif char == '<': new_pos = (pos[0], pos[1] - 1)
    else: new_pos = (pos[0] - 1, pos[1])
    return (new_pos[0] % dim[0], new_pos[1] % dim[1])

def get_next(grid):
    new_grid = [[[] for i in range(len(grid[0]))] for _ in range(len(grid))]
    for r, row in enumerate(grid):
        for c, blizzard in enumerate(row):
            for char in blizzard:
                new_pos = move_dir((r, c), char, (len(grid), len(grid[0])))
                new_grid[new_pos[0]][new_pos[1]].append(char)
    return new_grid

def neighbors(loc, grids):
    result = []
    for offset in ((0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)):
        new_loc = (loc[0] + offset[0], loc[1] + offset[1], loc[2] + 1)
        if new_loc[:2] == start or new_loc[:2] == dest:
            result.append(new_loc)
            continue
        if new_loc[0] < 0 or new_loc[1] < 0 or new_loc[0] >= len(grids[0]) or new_loc[1] >= len(grids[0][0]):
            continue
        if len(grids[new_loc[2]][new_loc[0]][new_loc[1]]) == 0: result.append(new_loc)
    return result

def solve(start, dest, grids):
    agenda = [start]
    found = set()
    while agenda:
        loc = agenda.pop(0)
        for neighbor in neighbors(loc, grids):
            if neighbor not in found:
                if neighbor[:2] == dest: return neighbor[2]
                found.add(neighbor)
                agenda.append(neighbor)

for i in range(depth):
    grids.append(get_next(grids[-1]))

# for i, grid in enumerate(grids):
#     print()
#     print("Minute", i)
#     disp(grid)

there = solve((-1, 0, 0), dest, grids)
back = solve((dest[0], dest[1], there), start, grids)
total = solve((-1, 0, back), dest, grids)
print(total)