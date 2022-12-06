from puzzle_input import read

data = read("input.txt", ['\n'])

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for line in data:
    one = line[:len(line) // 2]
    two = line[len(line) // 2:]
    for char in one:
        if char in two:
            total += alphabet.index(char) + 1
            break
print(total)

total = 0
for i in range(len(data) // 3):
    one = data[3 * i]
    two = data[3 * i + 1]
    three = data[3 * i + 2]
    for char in one:
        if char in two and char in three:
            total += alphabet.index(char) + 1
            break
print(total)