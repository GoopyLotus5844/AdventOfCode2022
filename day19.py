from puzzle_input import read
import math
import time

input = read("input.txt", ['\n', ':|\.', ' '])
time_limit = 32

names = ['ore', 'clay', 'obsidian', 'geode']

data = []
for line in input:
    data.append((
        (line[1][4], 0, 0, 0),
        (line[2][4], 0, 0, 0),
        (line[3][4], line[3][7], 0, 0),
        (line[4][4], 0, line[4][7], 0)
    ))

cache = dict()

def calc_wait(bot_type, res, bots, blueprint):
    to_go = [max(blueprint[bot_type][i] - res[i], 0) for i in range(3)]
    if any([to_go[i] != 0 and bots[i] == 0 for i in range(3)]): return -1
    wait = max([math.ceil(to_go[i] / bots[i]) if bots[i] != 0 else 0 for i in range(3)])
    return wait

#What resources will we have after waiting and then building bot?
def simulate_resources(res, bots, bot_type, wait, blueprint):
    if bot_type == -1: return [res[i] + wait * bots[i] for i in range(4)]
    return [res[i] + wait * bots[i] - blueprint[bot_type][i] for i in range(4)]

def add_bot(bots, bot_type):
    result = bots[:]
    result[bot_type] += 1
    return result

def get_key(res, bots, time):
    return (tuple(res), tuple(bots), time)

order = [0, 1, 1, 1, 2, 2, 3, 3]

def solve(res, bots, time, blueprint):
    key = get_key(res, bots, time)
    if key in cache: 
        return cache[key]

    max_geodes = 0
    for bot_type in range(4):

        if time > 20:
            if bot_type == 0 or bot_type == 1: continue

        wait = calc_wait(bot_type, res, bots, blueprint)
        if wait == -1: continue

        if time + wait + 1 > time_limit:
            result = simulate_resources(res, bots, -1, time_limit - time + 1, blueprint)[3]
            if result > max_geodes: 
                max_geodes = result
            continue

        args = (simulate_resources(res, bots, bot_type, wait + 1, blueprint), add_bot(bots, bot_type), time + wait + 1, blueprint)
        result = solve(*args)
        
        if result > max_geodes: 
            max_geodes = result

    cache[key] = max_geodes
    return max_geodes

# total = 0
# for i, blueprint in enumerate(data):
#     answer = solve([0, 0, 0, 0], [1, 0, 0, 0], 1, blueprint)
#     print("Completed blueprint", (i + 1))
#     total += answer * (i + 1)
#     cache.clear()

# print(total)

blueprint = data[0]
print(solve([0, 0, 0, 0], [1, 0, 0, 0], 1, blueprint))