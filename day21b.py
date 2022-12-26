from puzzle_input import read

data = read("input.txt", ['\n', ':'])

monkeys = dict()
for line in data:
    if isinstance(line[1], int): monkeys[line[0]] = line[1]
    else: monkeys[line[0]] = line[1].split(' ')

def do_math(a, b, op):
    if op == '+': return (a[0] + b[0], a[1] + b[1])
    if op == '-': return (a[0] - b[0], a[1] - b[1])
    if op == '*': return (b[1] * a[0] + a[1] * b[0], a[1] * b[1])
    if op == '/': return (a[0] / b[1], a[1] / b[1])

def equation(monkey):
    if monkey == 'humn': return (1, 0)
    formula = monkeys[monkey]
    if isinstance(formula, int): return (0, formula)
    return do_math(equation(formula[0]), equation(formula[2]), formula[1])

def solve(left, right):
    return (right[1] - left[1]) / (left[0] - right[0])

print(solve(equation(monkeys['root'][0]), equation(monkeys['root'][2])))