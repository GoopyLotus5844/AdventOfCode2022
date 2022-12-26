from puzzle_input import read

data = read("input.txt", ['\n'])

def answer(values):
    for i, val in enumerate(values):
        if val[1] == 0:
            zero_index = i
            break
    value_1 = values[(zero_index + 1000) % len(data)][1]
    value_2 = values[(zero_index + 2000) % len(data)][1]
    value_3 = values[(zero_index + 3000) % len(data)][1]
    return value_1 + value_2 + value_3

data = [val * 811589153 for val in data]
values = [(i, val) for i, val in enumerate(data)]
index = 0

for _ in range(10):
    for id in range(len(data)):
        while True:
            if values[index][0] == id: break
            index += 1
            if index == len(data): index = 0
        
        #moving current from index index to index dest
        offset = values[index][1]
        base_dest = index + offset

        if base_dest < 0: dest = (len(data) - 2) - (-base_dest - 1) % (len(data) - 1)
        elif base_dest >= len(data): dest = 1 + (base_dest - len(data)) % (len(data) - 1)
        else: dest = base_dest

        item = values.pop(index)
        values.insert(dest, item)

print(answer(values))