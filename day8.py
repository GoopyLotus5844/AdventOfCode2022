from puzzle_input import read

data = open("input.txt", "r").read().split('\n')
data = [[int(char) for char in line] for line in data]
count = 0

for r in range(len(data)):
    for c in range(len(data[r])):
        
        height = data[r][c]

        leftVis = True
        for l in range(0, c): 
            if data[r][l] >= height: 
                leftVis = False
                break
        
        rightVis = True
        for l in range(c+1, len(data[r])): 
            if data[r][l] >= height: 
                rightVis = False
                break
        
        topVis = True
        for l in range(0, r): 
            if data[l][c] >= height: 
                topVis = False
                break

        bottomVis = True
        for l in range(r+1, len(data)): 
            if data[l][c] >= height: 
                bottomVis = False
                break

        if leftVis or rightVis or topVis or bottomVis: count += 1

print(count)

max_score = 0
for r in range(len(data)):
    for c in range(len(data[r])):
        
        height = data[r][c]

        left = c
        for l in range(c-1, -1, -1): 
            if data[r][l] >= height: 
                left = abs(l - c)
                break
        
        right = len(data[0]) - c - 1
        for l in range(c+1, len(data[r])): 
            if data[r][l] >= height: 
                right = l - c
                break
        
        top = r
        for l in range(r-1, -1, -1): 
            if data[l][c] >= height: 
                top = abs(r - l)
                break

        bottom = len(data) - r - 1
        for l in range(r+1, len(data)): 
            if data[l][c] >= height: 
                bottom = l - r
                break

        prod = left * right * top * bottom
        if prod > max_score: max_score = prod

print(max_score)

