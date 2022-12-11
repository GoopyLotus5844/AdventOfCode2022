from puzzle_input import read

data = read("input.txt", ['\n', ' '])

cycle, x = 0, 1
check = {20, 60, 100, 140, 180, 220}
screen = [['.'] * 40 for i in range(6)]
total = 0

def draw_screen():
    row, column = cycle // 40, cycle % 40
    if cycle >= 240: return
    if abs(x - column) <= 1: screen[row][column] = "#"
    else: screen[row][column] = '.'

for line in data:
    cycle += 1
    if cycle in check: total += cycle * x
    if isinstance(line, list):
        draw_screen()
        cycle += 1
        if cycle in check: total += cycle * x
        x += line[1]
    draw_screen()

print(total)
for row in screen:
    print(''.join(row))