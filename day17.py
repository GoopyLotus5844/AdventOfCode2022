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

def print_board(board, start, end, nrock, pos):
    board_cpy = [row[:] for row in board]
    place(nrock, board_cpy, pos)
    rows = board_cpy[start:end][::-1]
    for row in rows: print(''.join("#" if val else '.' for val in row))

board = [[False] * width for _ in range(10000)]

top, jet_idx, nrock = 0, 0, 0
for i in range(2022):
    pos = (top + 3, 2)
    nrock %= len(rocks)
    while True:
        jet_idx %= len(data)
        
        if data[jet_idx] == '<': new_pos = (pos[0], pos[1] - 1)
        else: new_pos = (pos[0], pos[1] + 1)
        if in_bounds(nrock, new_pos[1]) and not intersecting(nrock, board, new_pos): pos = new_pos
        jet_idx += 1

        new_pos = (pos[0] - 1, pos[1])
        if not intersecting(nrock, board, new_pos): pos = new_pos
        else:
            new_top = place(nrock, board, pos)
            if new_top > top: top = new_top
            break
    nrock += 1
print(top)