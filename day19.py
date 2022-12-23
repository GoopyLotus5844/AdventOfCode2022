from puzzle_input import read
import math
import time

input = read("input.txt", ['\n', ':|\.', ' '])
time_limit = 24

data = []
for line in input:
    data.append((
        (line[1][4], 0, 0, 0),
        (line[2][4], 0, 0, 0),
        (line[3][4], line[3][7], 0, 0),
        (line[4][4], 0, line[4][7], 0)
    ))

cache = dict()

blueprint = data[1]

def calc_wait(bot_type, res, bots):
    to_go = [max(blueprint[bot_type][i] - res[i], 0) for i in range(3)]
    if any([to_go[i] != 0 and bots[i] == 0 for i in range(3)]): return -1
    wait = max([math.ceil(to_go[i] / bots[i]) if bots[i] != 0 else 0 for i in range(3)])
    return wait

#What resources will we have after waiting and then building bot?
def simulate_resources(res, bots, bot_type, wait):
    if bot_type == -1: return [res[i] + wait * bots[i] for i in range(4)]
    return [res[i] + wait * bots[i] - blueprint[bot_type][i] for i in range(4)]

def add_bot(bots, bot_type):
    result = bots[:]
    result[bot_type] += 1
    return result

def get_key(res, bots, time):
    return (tuple(res), tuple(bots), time)

def solve(res, bots, time):
    key = get_key(res, bots, time)
    if key in cache: 
        return cache[key]

    max_geodes = 0
    for bot_type in range(4):

        wait = calc_wait(bot_type, res, bots)
        if wait == -1: continue

        if time + wait + 1 > time_limit:
            result = simulate_resources(res, bots, -1, time_limit - time + 1)[3]
            cache[key] = result
            return result

        result = solve(simulate_resources(res, bots, bot_type, wait + 1), add_bot(bots, bot_type), time + wait + 1)
        if result > max_geodes: max_geodes = result

    cache[key] = max_geodes
    return max_geodes

start = time.time()
answer = solve([0, 0, 0, 0], [1, 0, 0, 0], 1)
print(time.time() - start)
print(answer)
