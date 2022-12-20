from puzzle_input import read
import time
data = read("input.txt", ['\n', 'valves|valve', ' |=|; |, '])

rates, big_graph = {}, {}
cache = {}

for line in data:
    rates[line[0][1]] = line[0][5]
    big_graph[line[0][1]] = line[1] if isinstance(line[1], list) else [line[1]]

def find_distances_bfs(start, little_graph, track_complete):
    agenda = [[start]]
    found = {start}
    while agenda:
        path = agenda.pop(0)
        loc = path[-1]
        for neighbor in big_graph[loc]:
            if neighbor not in found:
                if rates[neighbor] != 0 and (neighbor not in track_complete.get(start, [])):
                    little_graph.setdefault(start, []).append((neighbor, len(path)))
                    little_graph.setdefault(neighbor, []).append((start, len(path)))
                    track_complete.setdefault(start, set()).add(neighbor)
                    track_complete.setdefault(neighbor, set()).add(start)
                found.add(neighbor)
                new_path = path[:]
                new_path.append(neighbor)
                agenda.append(new_path)

def get_key(loc, not_opened, time):
    return (loc, frozenset(not_opened), time)

def node_value(node, time):
    return time * rates[node]

def solve(graph, loc, not_opened, time, depth):
    time -= 1
    pressure = node_value(loc, time)
    not_opened.remove(loc)
    if len(not_opened) == 0: return [(pressure, {loc})]

    paths = []
    for neighbor in graph[loc]:
        new_time = time - neighbor[1]
        if new_time <= 0 or not neighbor[0] in not_opened: continue
        paths.extend([(pressure + path[0], ({loc}.union(path[1]) if loc != 'AA' else path[1])) for path in solve(graph, neighbor[0], set(not_opened), new_time, depth+1)])
    if len(paths) == 0: paths = [(pressure, {loc})]

    return paths

little_graph, track_complete = {}, {}
for key in big_graph:
    if key == 'AA' or rates[key] != 0: 
        find_distances_bfs(key, little_graph, track_complete)

t = 27
not_opened = set(little_graph.keys())
result = solve(little_graph, 'AA', not_opened, t, 0)
no_duplicates = dict()

for path in result:
    key = frozenset(path[1])
    if key in no_duplicates:
        val = no_duplicates[key]
        if path[0] > val: no_duplicates[key] = path[0]
    else: no_duplicates[key] = path[0]

max = 0
for first in no_duplicates:
    for second in no_duplicates:
        if first.isdisjoint(second):
            total = no_duplicates[first] + no_duplicates[second]
            if total > max: max = total

print(max)