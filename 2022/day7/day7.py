lines = []
with open("test.txt", "r") as file:
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
        for key in d.keys():
            if key in pwd:
                d[key] += size
        d[pwd] = size
    print(path, d)



print(d)
total = 0
for dir in d:
    if d[dir] <= 100000:
        total += d[dir]
print(total)

#1266594
