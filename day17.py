from puzzle_input import read

data = read("input.txt", [])
width = 7

rocks = (
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1))
)

rock_w = (4, 3, 3, 1, 2)
rock_h = (1, 3, 3, 4, 2)

def place(nrock, board, pos):
    for tile in rocks[nrock]:
        board[pos[1] + tile[1]][pos[0] + tile[0]] = True

def in_bounds(nrock, x):
    return 0 <= x <= width - rock_w[nrock]

def intersecting(nrock, board, pos):
    rows = board[pos[1] : pos[1] + rock_h]
    for r, row in enumerate(rows):
        for c in range(width): if rocks[nrock]

board = [[False] * width for i in range(10000)]

