from puzzle_input import read

data = read("input.txt", ['\n'])

values = {data[i]: i for i in range(len(data))}

def display(values):
    as_list = []
    for i in range(len(data)):
        for key in values:
            if values[key] == i: as_list.append(key)
    print(as_list)

def verify(values):
    values_list = []
    for key in values: values_list.append(values[key])
    return len(set(values_list)) == len(values_list)

def find_value_with_index(values, index):
    for key in values:
        if values[key] == index: return key

def answer(values):
    zero_index = values[0]
    value_1 = find_value_with_index(values, (zero_index + 1000) % len(data))
    value_2 = find_value_with_index(values, (zero_index + 2000) % len(data))
    value_3 = find_value_with_index(values, (zero_index + 3000) % len(data))
    return value_1 + value_2 + value_3

def new_answer(values):
    for i, val in enumerate(values):
        if val == 0:
            zero_index = i
            print("I am right here")
            break

    value_1 = values[(zero_index + 1000) % len(data)]
    value_2 = values[(zero_index + 1000) % len(data)]
    value_3 = values[(zero_index + 1000) % len(data)]
    return value_1 + value_2 + value_3

for current in data:

    if not verify(values):
        print("this is very bad")

    #moving current from index a to index b
    a = values[current]
    b = a + current
    if b < 0: b += len(data) - 1
    elif b >= len(data): b -= len(data) + 1
    values[current] = b

    if b > a:
        for key in data:
            if key == current: continue
            initial = values[key]
            if initial > a and initial <= b:
                values[key] -= 1
    elif b < a:
        for key in data:
            if key == current: continue
            initial = values[key]
            if initial < a and initial >= b:
                values[key] += 1

print(answer(values))