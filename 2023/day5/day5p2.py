lines = []
res = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())

seeds = [int(seed) for seed in lines[0].split()[1:]]
# seeds = [3561206012, 483360452]
seeds = [3900000000, 4100000000]
        #4002148012

# for i in range(len(seeds)):
#     if i % 2 == 1:
#         seeds[i] = seeds[i] + seeds[i-1]
seeds[1] = seeds[1] + seeds[0]

# seeds = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

step = 100
seeds = list(range(int(seeds[0]), int(seeds[1]), step))

# for i in range(len(seeds)):
#     seeds[i] = list(range(seeds[i][0], seeds[i][1], step))

def process(seed):
    changed = False
    for i in range(3, len(lines)):
        if changed and lines[i] != "":
            continue
        else:
            changed = False
        start = 0
        end = 0
        change = 0
        if lines[i] == '' or lines[i][0].isalpha():
            continue
        values = lines[i].split()
        start = int(values[1]) 
        end = int(values[1]) + int(values[2]) - 1
        change = int(values[0]) - int(values[1])
        if start <= int(seed) <= end:
            seed += change
            changed = True
        else:
            continue
    return seed

# print(seeds)
ranges = []
smallest = float('inf')
for i in range(len(seeds)):
    location = process(seeds[i])
    if location < smallest:
        smallest = location
        ranges.append(i)

print(ranges[-1])
print(smallest)


# ranges = []
# for i in range(len(seeds)):
#     smallest = float("inf")
#     for j in range(len(seeds[i])):
#         location = process(seeds[i][j])
#         smallest = min(smallest, location)
#     res.append(smallest)
#     ranges.append(i)

# 


#29102684
#17737743
#17729743