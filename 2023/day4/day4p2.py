lines = []
winning = []
hand = []
d ={}
with open("input.txt", "r") as file:
    while line:= file.readline():
        lines.append(line.strip("Card ").strip())

for i in range(len(lines)):
    winning.append(lines[i].split("|")[0].strip().split(" "))
    hand.append(lines[i].split("|")[1].strip().split(" "))
    d[i] = 1

total = 0
for x in range(len(hand)-1):
    extras = 0
    xx = x
    for y in range(len(hand[x])):
        if hand[x][y] == "":
            continue
        if hand[x][y] in winning[x]:
            extras += 1
    print(extras)

    for i in range(extras):
        xx += 1
        d[xx] += d[x]

sum = 0
for i in d.values():
    sum+=i
print(sum)
#{0:1, 1:2, 2:4, 3:8, 4:14, 5:1}