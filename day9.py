from puzzle_input import read
data = read("input.txt", ['\n', ' '])

def adj(one, two):
    return abs(one[0] - two[0]) <= 1 and abs(one[1] - two[1]) <= 1

def sign(num):
    return 0 if num == 0 else num // abs(num)

knots = [[0, 0] for i in range(2)]
visited = set()

for line in data:
    for m in range(line[1]):
        if line[0] == 'U': knots[0][0] -= 1
        elif line[0] == 'D': knots[0][0] += 1
        elif line[0] == 'L': knots[0][1] -= 1
        else: knots[0][1] += 1

        for i in range(1, len(knots)):
            current, follow = knots[i], knots[i - 1]
            if not adj(current, follow):
                current[0] += sign(follow[0] - current[0])
                current[1] += sign(follow[1] - current[1])
        visited.add((knots[-1][0], knots[-1][1]))

print(len(visited))