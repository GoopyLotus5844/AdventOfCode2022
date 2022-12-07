from puzzle_input import read

data = read("input.txt", ['\n', ' '])

tree = dict()
stack = [tree]

index = 2
for line in data[2:]:
    current = stack[-1]
    if line[0] != '$':
        if line[0] == 'dir':
            current[line[1]] = dict()
        else: current[line[1]] = line[0]
    elif line[1] == 'cd':
        if line[2] == '..': stack.pop()
        else: stack.append(current[line[2]])

sizes = []
def calc_sizes(dir):
    total = 0
    for key in dir:
        if isinstance(dir[key], int): total += dir[key]
        else: total += calc_sizes(dir[key])
    sizes.append(total)
    return total

calc_sizes(tree)
total = 0
for size in sizes:
    if size < 100000: total += size
print(total)

everything_size = sizes[-1]
difference = everything_size - 40000000
good = []
for size in sizes:
    if size > difference: good.append(size)
print(sorted(good)[0])