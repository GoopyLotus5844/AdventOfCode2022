from puzzle_input import read

data = read("input.txt", [])
width = 7

rocks = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (0, 1), (1, 0), (1, 1))
)

rock_w = (4, 3, 3, 1, 2)
rock_h = (1, 3, 3, 4, 2)

def place(nrock, board, pos):
    for tile in rocks[nrock]:
        board[tile[0] + pos[0]][tile[1] + pos[1]] = True
    return pos[0] + rock_h[nrock]

def in_bounds(nrock, x):
    return 0 <= x <= width - rock_w[nrock]

def intersecting(nrock, board, pos):
    if pos[0] < 0: return True
    for tile in rocks[nrock]:
        if board[tile[0] + pos[0]][tile[1] + pos[1]]: return True
    return False

def neighbors(loc, ceiling):
    result = []
    for offset in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        neighbor = (loc[0] + offset[0], loc[1] + offset[1])
        if neighbor[0] < 0 or neighbor[0] >= ceiling or neighbor[1] < 0 or neighbor[1] >= width: continue
        result.append(neighbor)
    return result

def flood_fill(board, ceiling):
    start = (ceiling - 1, 0)
    agenda = [start]
    found = {start}
    while agenda:
        loc = agenda.pop(0)
        for neighbor in neighbors(loc, ceiling):
            if neighbor not in found and not board[neighbor[0]][neighbor[1]]:
                found.add(neighbor)
                agenda.append(neighbor)
    return frozenset({(ceiling - point[0], point[1]) for point in found})

def get_key(board, top, jet_idx, nrock):
    shape = flood_fill(board, top + 1)
    return (shape, jet_idx, nrock)

board = [[False] * width for _ in range(100000)]

cache = dict()
heights = []
simulate = 1000000000000

top, jet_idx, nrock = 0, 0, 0
for i in range(simulate):
    pos = (top + 3, 2)
    key = get_key(board, top, jet_idx, nrock % len(rocks))

    if key in cache:
        last = cache[key]
        rep_height = top - heights[last - 1]
        rep_rocks = nrock - last
        reps = (simulate - nrock) // rep_rocks
        answer = top + (rep_height) * reps
        remainder = (simulate - nrock) % rep_rocks
        answer += heights[last + remainder - 1] - heights[last - 1]
        print(answer)
        break

    while True:
        n = nrock % len(rocks)
        jet_idx %= len(data)
        
        if data[jet_idx] == '<': new_pos = (pos[0], pos[1] - 1)
        else: new_pos = (pos[0], pos[1] + 1)
        if in_bounds(n, new_pos[1]) and not intersecting(n, board, new_pos): pos = new_pos
        jet_idx += 1

        new_pos = (pos[0] - 1, pos[1])
        if not intersecting(n, board, new_pos): pos = new_pos
        else:
            new_top = place(n, board, pos)
            if new_top > top: top = new_top
            break

    cache[key] = nrock
    heights.append(top)
    nrock += 1