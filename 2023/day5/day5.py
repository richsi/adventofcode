lines = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())

seeds = [int(seed) for seed in lines[0].split()[1:]]

res = []
for i in range(len(seeds)):
    changed = False
    seed = seeds[i]
    for j in range(3,len(lines)):
        if changed and lines[j] != "":
            continue
        else:
            changed = False
        start = 0
        end = 0
        change = 0
        if lines[j] == '' or lines[j][0].isalpha():
            print("skip")
            continue
        values = lines[j].split()
        start = int(values[1]) 
        end = int(values[1]) + int(values[2]) - 1
        change = int(values[0]) - int(values[1])
        print(start, end, change, seed)
        if start <= int(seed) <= end:
            seed += change
            changed = True
        else:
            continue
    res.append(seed)
    print()

print(min(res))
