from puzzle_input import read

data = read("input.txt", ['\n', ':'])

monkeys = dict()
for line in data:
    if isinstance(line[1], int): monkeys[line[0]] = line[1]
    else: monkeys[line[0]] = line[1].split(' ')

def do_math(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def solve(monkey):
    formula = monkeys[monkey]
    if isinstance(formula, int): return formula
    return do_math(solve(formula[0]), solve(formula[2]), formula[1])

print(solve('root'))