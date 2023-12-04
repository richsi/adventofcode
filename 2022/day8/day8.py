lines=[]
with open("test.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())
    
outside = (len(lines) * 2) + ((len(lines[0]) - 2) * 2)

inside = 0
#check horizontal
for row in range(1, len(lines)-1):
    for col in range(1, len(lines[0])-1):
        