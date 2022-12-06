from puzzle_input import read

data = read("input.txt", [])

def solve(size):
    for i in range(size, len(data)):
        chars = data[i-size:i]
        double = False
        for x in range(len(chars)):
            for y in range(x + 1, len(chars)):
                if chars[x] == chars[y]: 
                    double = True
                    break
        if not double: return i

print(solve(4))
print(solve(14))