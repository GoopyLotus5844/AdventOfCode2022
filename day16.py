from puzzle_input import read
data = read("input.txt", ['\n', 'valves|valve', ' |=|; |, '])

POWER = 8
rates, big_graph = {}, {}

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

def node_value(node, time):
    return time * rates[node]

def solve(graph, loc, not_opened, time):
    if time <= 0: return 0
    time -= 1

    pressure = node_value(loc, time)
    not_opened.remove(loc)
    if len(not_opened) == 0: return pressure

    neighbors = [neighbor for neighbor in graph[loc] if neighbor[0] in not_opened]
    neighbors.sort(key=lambda n: node_value(n[0], time - n[1]))
    to_check = neighbors[-min(len(neighbors), POWER):]

    return pressure + max([solve(graph, neighbor[0], set(not_opened), time - neighbor[1]) for neighbor in to_check])


little_graph, track_complete = {}, {}
for key in big_graph:
    if key == 'AA' or rates[key] != 0: 
        find_distances_bfs(key, little_graph, track_complete)

time = 31
not_opened = set(little_graph.keys())
result = solve(little_graph, 'AA', not_opened, time)

print(result)
