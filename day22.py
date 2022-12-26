data = open("input.txt", "r").read().split('\n\n')

grid = data[0].split("\n")

def parse_path(ins):
    index, parsed = 0, []
    while True:
        l, r = ins.find('L', index), ins.find('R', index)
        if l == -1 and r == -1:
            parsed.append(int(ins[index:]))
            return parsed
        next = min(l, r) if r != -1 and l != -1 else (r if l == -1 else l)
        parsed.append(int(ins[index:next]))
        parsed.append(ins[next])
        index = next + 1

row_bounds = [(len(s) - len(s.lstrip()), len(s.rstrip()) - 1) for s in grid]
col_bounds = []
for c in range(len(grid[0])):
    row, start, end = 0, -1, -1
    while True:
        if start == -1:
            if grid[row][c] != ' ': start = row
        elif row >= len(grid) or c >= len(grid[row]) or grid[row][c] == ' ': 
            end = row - 1
            break
        row += 1
    col_bounds.append((start, end))

path = parse_path(data[1])
facing = 0
pos = (0, row_bounds[0][0])

for step in path:
    if isinstance(step, int):
        for _ in range(step):
            rbounds = row_bounds[pos[0]]
            cbounds = col_bounds[pos[1]]
            row, col = pos[0], pos[1]
            if facing == 0:
                col += 1
                if col > rbounds[1]: col = rbounds[0]
            elif facing == 1:
                row += 1
                if row > cbounds[1]: row = cbounds[0]
            elif facing == 2:
                col -= 1
                if col < rbounds[0]: col = rbounds[1]
            elif facing == 3:
                row -= 1
                if row < cbounds[0]: row = cbounds[1]
            if grid[row][col] != '#': pos = (row, col)
            else: break
    else:
        if step == 'L': facing -= 1
        else: facing += 1
        facing %= 4

answer = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facing
print(answer)