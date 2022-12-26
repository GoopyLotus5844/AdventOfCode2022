data = open("input.txt", "r").read().split('\n\n')
grid = data[0].split("\n")

#   1 2
#   3
# 4 5
# 6 
# (tile, edge#): (rel_c, rel_c) -> (tile, rel_r, rel_c, facing)

size = 50
movement = {
    (1, 2): lambda r, c: (4, size - r - 1, 0, 0),
    (1, 3): lambda r, c: (6, c, 0, 0),
    (2, 0): lambda r, c: (5, size - r - 1, size - 1, 2),
    (2, 1): lambda r, c: (3, c, size - 1, 2),
    (2, 3): lambda r, c: (6, size - 1, c, 3),
    (3, 0): lambda r, c: (2, size - 1, r, 3),
    (3, 2): lambda r, c: (4, 0, r, 1),
    (4, 2): lambda r, c: (1, size - r - 1, 0, 0),
    (4, 3): lambda r, c: (3, c, 0, 0),
    (5, 0): lambda r, c: (2, size - r - 1, size - 1, 2),
    (5, 1): lambda r, c: (6, c, size - 1, 2),
    (6, 0): lambda r, c: (5, size - 1, r, 3),
    (6, 1): lambda r, c: (2, 0, c, 1),
    (6, 2): lambda r, c: (1, 0, r, 1)
}

face_to_coord = {
    1: (0, 1),
    2: (0, 2),
    3: (1, 1),
    4: (2, 0),
    5: (2, 1),
    6: (3, 0)
}
coord_to_face = {face_to_coord[key]: key for key in face_to_coord}

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

def get_face_coord(pos):
    return (pos[0] // size, pos[1] // size)

def get_relative_pos(pos, face_coord):
    return (pos[0] - face_coord[0] * size, pos[1] - face_coord[1] * size)

def get_abs_pos(pos, face_coord):
    return (face_coord[0] * size + pos[0], face_coord[1] * size + pos[1])

def move_in_dir(pos, dir):
    if dir == 0: return (pos[0], pos[1] + 1)
    if dir == 1: return (pos[0] + 1, pos[1])
    if dir == 2: return (pos[0], pos[1] - 1)
    return (pos[0] - 1, pos[1])

def get_edge_number(face_pos):
    if face_pos[0] < 0: return 3
    if face_pos[0] >= size: return 1
    if face_pos[1] < 0: return 2
    return 0

def dir_char(dir):
    if dir == 0: return '>'
    if dir == 1: return 'V'
    if dir == 2: return '<'
    return '^'

path = parse_path(data[1])
facing, pos = 0 ,(0, 50)

for step in path:
    if isinstance(step, int):
        for _ in range(step):
            old_face_coord = get_face_coord(pos)
            new_pos = move_in_dir(pos, facing)
            new_face_coord = get_face_coord(new_pos)
            if old_face_coord != new_face_coord:
                rel_to_old = get_relative_pos(new_pos, old_face_coord)
                edge_number = get_edge_number(rel_to_old)
                movement_key = (coord_to_face[old_face_coord], edge_number)

                if movement_key in movement:
                    moved = movement[movement_key](*rel_to_old)
                    new_pos = get_abs_pos((moved[1], moved[2]), face_to_coord[moved[0]])
                    if grid[new_pos[0]][new_pos[1]] != '#':
                        pos = new_pos
                        facing = moved[3]
                elif grid[new_pos[0]][new_pos[1]] != '#': pos = new_pos
            elif grid[new_pos[0]][new_pos[1]] != '#': pos = new_pos
    else:
        if step == 'L': facing -= 1
        else: facing += 1
        facing %= 4

answer = (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + facing
print(answer)