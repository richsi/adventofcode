with open("input.txt", "r") as file:
    lines = file.readlines()

cords = set()
nums = "0123456789."   
for x, line in enumerate(lines):
    for y, char in enumerate(line.strip()):
        if char not in nums:
            for xx in range(x-1, x+2):
                for yy in range(y-1, y+2):
                    if lines[xx][yy].isdigit():
                        col = yy
                        while(lines[xx][col].isdigit()):
                            col -= 1
                        cords.add((xx, col+1))

total = 0
for cord in cords:
    part = ""
    y = cord[1]
    while(y < len(lines[cord[0]]) and lines[cord[0]][y].isdigit()):
        part += lines[cord[0]][y]
        y += 1
    total += int(part)
print(total)