from puzzle_input import read, tryConvert
from math import gcd

data = read("input.txt", ['\n\n', '\n'])

monkeys = []
for monkey in data:
    monkeys.append({
        'items': [int(w) for w in monkey[1].split(':')[1].split(',')],
        'operation': monkey[2].split(':')[1].split(' ')[-3:],
        'test': int(monkey[3].split(' ')[-1]),
        'true': int(monkey[4].split(' ')[-1]),
        'false': int(monkey[5].split(' ')[-1]),
    })

def eval_operation_arg(old, arg):
    return int(arg) if isinstance(tryConvert(arg), int) else old

def eval_worry(old, operation):
    first, second = eval_operation_arg(old, operation[0]), eval_operation_arg(old, operation[2])
    return first + second if operation[1] == '+' else first * second

def lcm(tests):
    lcm = 1
    for i in tests:
        lcm = lcm * i // gcd(lcm, i)
    return lcm

def solve(rounds, manage_worry):
    inspected = [0] * len(monkeys)
    for _ in range(rounds):
        for m, monkey in enumerate(monkeys):
            inspected[m] += len(monkey['items'])
            for item in monkey['items']:
                new = manage_worry(eval_worry(item, monkey['operation']))
                result = 'true' if new % monkey['test'] == 0 else 'false'
                monkeys[monkey[result]]['items'].append(new)
            monkey['items'] = []
    result = sorted(inspected)
    return result[-1] * result[-2]

# print(solve(20, lambda x: x // 3))
mod = lcm([monkey['test'] for monkey in monkeys])
print(solve(10000, lambda x: x % mod))