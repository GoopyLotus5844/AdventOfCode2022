from puzzle_input import read

data = read("input.txt", ['\n\n', '\n'])

for pair in data:
    pair[0] = eval(pair[0])
    pair[1] = eval(pair[1])

def make_list(item):
    if isinstance(item, int): return [item]
    return item

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return 1
        if left == right: return 2
        return 0
    elif isinstance(left, list) and isinstance(right, list):
        for i, item in enumerate(left):
            if i >= len(right): return False
            result = compare(item, right[i])
            if result == 0 or result == 1: return result
        if len(left) == len(right): return 2
        return 1

    return compare(make_list(left), make_list(right))

print(sum([i + 1 for i, pair in enumerate(data) if compare(pair[0], pair[1]) == 1]))

all_packets = []
for pair in data:
    all_packets.append(pair[0])
    all_packets.append(pair[1])

div_a, div_b = [[2]], [[6]]
total_a, total_b = 0, 0
for i, packet in enumerate(all_packets):
    total_a += compare(packet, div_a)
    total_b += compare(packet, div_b)

print((total_a + 1) * (total_b + 2))