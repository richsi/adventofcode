with open("input.txt", "r") as file:
    lines = file.readlines()
    
cords = []
for x, line in enumerate(lines):
    for y, char in enumerate(line.strip()):
        if char == "*":
            gears= set()
            for xx in range(x-1, x+2):
                for yy in range(y-1, y+2):
                    if lines[xx][yy].isdigit():
                        col = yy
                        while(lines[xx][col].isdigit()):
                            col -= 1
                        gears.add((xx, col+1))
            if len(gears) == 2:
                cords.append(gears)
total = 0
for cord in cords:
    ratio = []
    for gear in cord:
        part = ""
        y = gear[1]
        while(y < len(lines[gear[0]]) and lines[gear[0]][y].isdigit()):
            part += lines[gear[0]][y]
            y += 1
        ratio.append(int(part))
    total += ratio[0] * ratio[1]
print(total)
