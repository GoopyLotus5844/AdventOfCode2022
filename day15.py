from puzzle_input import read

data = read("input.txt", ['\n', ' |,|=|:'])
pairs = [((line[3], line[6]), (line[13], line[16])) for line in data]

def calc_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def in_interval(point, intervals):
    for interval in intervals:
        if interval[0] <= point <= interval[1]: return True
    return False

def compute_intervals(pairs, row):
    intervals = []
    for pair in pairs:
        dist = calc_dist(pair[0], pair[1])
        dx = dist - abs(row - pair[0][1])
        if dx < 0: continue
        intervals.append((pair[0][0] - dx, pair[0][0] + dx))
    return intervals

def simplify_intervals(intervals):
    while True:
        found = False
        for a, intA in enumerate(intervals):
            for intB in intervals[a + 1:]:
                if intB[0] >= intA[0] and intB[1] <= intA[1]: 
                    intervals.remove(intB)
                    found = True
                elif intA[0] >= intB[0] and intA[1] <= intB[1]: 
                    intervals.remove(intA)
                    found = True
                elif intA[1] >= intB[0] and intA[0] <= intB[1]:
                    intervals.remove(intA)
                    intervals.remove(intB)
                    intervals.append((min(intA[0], intB[0]), max(intA[1], intB[1])))
                    found = True
                if found: break
            if found: break
        if not found: break

row = 2000000
intervals = compute_intervals(pairs, row)
simplify_intervals(intervals)

beacons = 0
for beacon in set([pair[1] for pair in pairs]):
    if beacon[1] == row and in_interval(beacon[0], intervals): beacons += 1

total = sum([interval[1] - interval[0] + 1 for interval in intervals])
print(total - beacons)

for row in range(4000000):
    intervals = compute_intervals(pairs, row)
    simplify_intervals(intervals)
    if len(intervals) == 2:
        x = intervals[0][1] + 1 if intervals[0][0] < intervals[1][0] else intervals[1][1] + 1
        print(x * 4000000 + row)
        break