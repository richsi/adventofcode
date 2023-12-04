lines = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())
        
d = dict()
path = ["/"]
for i in range(1, len(lines)):
    size = 0

    if lines[i][2:4] == 'cd':
        if lines[i][5:7] == '..':
            path.pop()
        else:
            path.append(lines[i][5:]+"/")

    elif lines[i][2:4] == 'ls':
        for j in range(i+1, len(lines)):
            if lines[j][0] == '$':
                break
            elif lines[j][0].isdigit():
                size += int(lines[j].split()[0])
        pwd = "".join(path)
        # print(pwd)
        for key in d.keys():
            if key in pwd:
                d[key] += size
        d[pwd] = size
# print(d)
remaining = 70000000 - d.get("/", 0)
goal = 30000000 - remaining
print(goal)
options = []
for dir in d.keys():
    if d[dir] >= goal:
        options.append(d[dir])
print(min(options))