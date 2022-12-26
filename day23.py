from puzzle_input import read

data = read("input.txt", ['\n'])
elves = set()
for r, line in enumerate(data):
    for c, char in enumerate(line):
        if char == '#': elves.add((r, c))

directions = ((-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (-1, -1), (1, -1), (0, 1), (-1, 1), (1, 1))

def add(pos, offset):
    return (pos[0] + offset[0], pos[1] + offset[1])

def has_neighbors(pos, elves):
    return any([add(pos, offset) in elves for offset in directions])

def has_neighbors_cardinal(pos, cdir):
    return any([add(pos, offset) in elves for offset in directions[3*cdir:3*cdir+3]])

def cdir_offset(cdir):
    return directions[3 * cdir]

def get_bounds(elves):
    minr, maxr, minc, maxc = 1000, 0, 1000, 0
    for elf in elves:
        if elf[0] < minr: minr = elf[0]
        if elf[0] > maxr: maxr = elf[0]
        if elf[1] < minc: minc = elf[1]
        if elf[1] > maxc: maxc = elf[1]
    return (minr, maxr, minc, maxc)

def disp(elves):
    minr, maxr, minc, maxc = get_bounds(elves)
    grid = [['.'] * (maxc - minc + 1) for _ in range(maxr - minr + 1)]
    for elf in elves:
        grid[elf[0] - minr][elf[1] - minc] = '#'
    for row in grid:
        print(''.join(row))

#N, S, W, E
order = [0, 1, 2, 3]
iter = 0

while True:
    iter += 1
    proposed_count = dict()
    elf_proposed = dict()
    moved = False
    for elf in elves:
        if not has_neighbors(elf, elves): continue
        moved = True
        for cdir in order:
            if not has_neighbors_cardinal(elf, cdir):
                proposed = add(elf, cdir_offset(cdir))
                if proposed in proposed_count: proposed_count[proposed] += 1
                else: proposed_count[proposed] = 1
                elf_proposed[elf] = proposed
                break
    if not moved: break

    new_elves = set()
    for elf in elves:
        if not elf in elf_proposed:
            new_elves.add(elf)
            continue
        proposed = elf_proposed[elf]
        if proposed_count[proposed] > 1: 
            new_elves.add(elf)
            continue
        new_elves.add(proposed)
    elves = new_elves
    order.append(order.pop(0))

minr, maxr, minc, maxc = get_bounds(elves)
part1 = (maxr - minr + 1) * (maxc - minc + 1) - len(elves)
print(iter)