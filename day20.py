from puzzle_input import read

data = read("input.txt", ['\n'])

def answer(values):
    for i, val in enumerate(values):
        if val == 0:
            zero_index = i
            break
    value_1 = values[(zero_index + 1000) % len(data)]
    value_2 = values[(zero_index + 2000) % len(data)]
    value_3 = values[(zero_index + 3000) % len(data)]
    return value_1 + value_2 + value_3

# data = [val * 811589153 for val in data]
values = data[:]
index = 0

for _ in range(1):
    for current in data:
        while True:
            if values[index] == current: break
            index += 1
            if index == len(data): index = 0
        
        #moving current from index index to index dest
        base_dest = index + current
        dest = base_dest % len(data)
        if base_dest < 0: dest -= -base_dest // len(data) + 1
        elif base_dest >= len(data): dest += base_dest // len(data)

        values.pop(index)
        values.insert(dest, current)
        if dest < index: index += 1

print(answer(values))