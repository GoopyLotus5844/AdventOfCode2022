from puzzle_input import read

data = read("input.txt", ['\n', ' '])
data = [[line[1], line[3], line[5]] for line in data] 

input = [
    ['N', 'R', 'J', 'T', 'Z', 'B', 'D', 'F'],
    ['H', 'J', 'N', 'S', 'R'],
    ['Q', 'F', 'Z', 'G', 'J', 'N', 'R', 'C'],
    ['Q', 'T', 'R', 'G', 'N', 'V', 'F'],
    ['F', 'Q', 'T', 'L'],
    ['N', 'G', 'R', 'B', 'Z', 'W', 'C', 'Q'],
    ['M', 'H', 'N', 'S', 'L', 'C', 'F'],
    ['J', 'T', 'M', 'Q', 'N', 'D'],
    ['S', 'G', 'P']
]

def print_ans(boxes):
    str = ""
    for stack in boxes:
        str += stack[-1]
    print(str)

boxes = [stack[::-1] for stack in input]
for line in data:
    for i in range(line[0]):
        box = boxes[line[1] - 1].pop()
        boxes[line[2] - 1].append(box)
print_ans(boxes)

boxes = [stack[::-1] for stack in input]
for line in data:
    start = len(boxes[line[2] - 1])
    for i in range(line[0]):
        box = boxes[line[1] - 1].pop()
        boxes[line[2] - 1].insert(start, box)
print_ans(boxes)